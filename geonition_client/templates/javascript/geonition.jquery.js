
/*
The base object for geonition javascript function
all functions should be under gnt.<app name>.<function name>(<params>)
*/
var gnt = {};


/*
Version of applications

Each application has to update this object.
*/
gnt.app_version = {};
gnt.app_version.geonition_client = "2.0.0";

/*
configure parameters

default values below
*/
gnt.config = {};
gnt.config.CSRF_cookie_name = "{{ CSRF_Cookie_Name }}";
gnt.config.api_full_url = "{{ method }}{{ host }}";


/*
added to all AJAX calls to the server
*/
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken",
                             getCookie(gnt.config.CSRF_cookie_name));
    }
});

{% for client in geonition_clients %}
    {{ client }}
{% endfor %}

