from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.template import TemplateDoesNotExist

import jsmin #to minify the javascript

def javascript_api(request):
    """
    This function returns the javascript client
    that was requested.
    
    The client will be a combination of the javascript
    templates found in settings under JAVASCRIPT_CLIENT_TEMPLATES
    """
    # get the templates
    js_templates = getattr(settings, 'JAVASCRIPT_CLIENT_TEMPLATES', [])
    
    # render the clients to strings
    js_clients = []
    for template in js_templates:        
        try:
            js_clients.append(
                render_to_string(
                    template,
                    RequestContext(request)
                ))
        except TemplateDoesNotExist:
            pass
    
    pre_url = "https://"
    if not request.is_secure():
        pre_url = "http://"

    host = request.get_host()
    
    js_string = render_to_string(
                    "javascript/geonition.jquery.js",
                    RequestContext(request,
                              {'geonition_clients': js_clients,
                               'host': host,
                               'method': pre_url,
                               'CSRF_Cookie_Name' : getattr(settings, "CSRF_COOKIE_NAME","csrftoken")
                               }
                              ))
    
    if getattr(settings, 'DEBUG', False):
        minified_js = js_string
    else:
        minified_js = jsmin.jsmin(js_string)
    
    # return the clients in one file
    
    response = HttpResponse(minified_js,
                            mimetype="application/javascript")
    
    return response


def test_api(request):
    """
    This view function returns an HTML page that loads the
    dojo api and the softgis.js so that the API javascript
    functions can be tested from a javascript console.
    """
    
    return render_to_response("test/test.html",
                              context_instance = RequestContext(request))
    
    
def csrf(request):
    """
    This view returns a csrf token which can be used to send
    other POST requests to the REST api directly without using any
    Javascript library provided.
    """
    return render_to_response("csrf.txt",
                              context_instance = RequestContext(request),
                              mimetype="text/plain")
