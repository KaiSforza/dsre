from django.http import HttpResponse
import logging

log = logging.getLogger(__name__)

def index(request, name='john'):
    lang = request.GET.get('lang', 'en')
    jsonmsg = '{"message": "Hola %s!"}' % name
    if request.method == "GET":
        if request.META.get('HTTP_ACCEPT', None) == "application/json":
            log.debug("returning a json object")
            if lang == "es":
                return HttpResponse(jsonmsg)
            else:
                return HttpResponse('{"message": "Good morning"}')
        else:
            log.debug("returning an html object")
            if lang == "es":
                return HttpResponse(f"<p>Hola, {name}</p>")
            else:
                return HttpResponse("<p>Hello, World</p>")
