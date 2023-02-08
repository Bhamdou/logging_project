from django.shortcuts import render
import logging
from django.http import HttpResponse
# Create your views here.
logger = logging.getLogger(__name__)
def hello_world(request):
    # division = x / 100
    logger.warning("i am a tea pot")
    return HttpResponse(f"Hello World")