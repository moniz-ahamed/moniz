from django.http import HttpResponse
from django.shortcuts import render
def homePage (request):
    return render (request, "index.html")

def aboutUs (request):
    return HttpResponse("welcome to moniztech")
def course (request):
    return HttpResponse("<b>welcome to moniztech_course<b/>")
def courseDetails (request, courseid):
    return HttpResponse (courseid)
