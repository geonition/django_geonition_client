/*
All functions should be gradually added to this
object so that it can be used side by side with
other libraries, and also minimize conflict with
the users own functions and method.
*/
var gnt = {};


var CSRF_Cookie_Name   = "{{ CSRF_Cookie_Name }}";
var api_full_url = "{{ method }}{{ host }}";

function getCookie(c_name) {
    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++) {
        x = ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x = x.replace(/^\s+|\s+$/g,"");
        
        if (x === c_name) {
            return unescape(y);
        }
    }
}

{% block library_specific_block %}
{% endblock %}
