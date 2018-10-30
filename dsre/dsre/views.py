from django.http import HttpResponse
import logging

log = logging.getLogger(__name__)

def index(request):
    if request.method == "GET":
        if request.META['HTTP_ACCEPT'] == "application/json":
            log.debug("returning a json object")
            return HttpResponse('{"message": "Good morning"}')
        else:
            log.debug("returning an html object")
            return HttpResponse("<p>Hello, World</p>")
