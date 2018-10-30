from django.http import HttpResponse
import logging

log = logging.getLogger(__name__)

def index(request):
    if request.method == "GET":
        if request.META['HTTP_ACCEPT'] == "application/json":
            logging.debug("returning a json object")
            return HttpResponse('{"message": "Good morning"}')
        else:
            logging.debug("returning an html object")
            return HttpResponse("<p>Hello, World</p>")
