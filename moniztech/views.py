from django.http import HttpResponse

def aboutUs (request):
    return HttpResponse("welcome to moniztech")
def course (request):
    return HttpResponse("<b>welcome to moniztech_course<b/>")
