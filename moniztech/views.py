from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title': 'My Courses',
        'clist': ['PHP', 'Java', 'Django'],
        'course_details': [
            {'course': 'PHP', 'price': '$100'},
            {'course': 'Java', 'price': '$200'},
            {'course': 'Django', 'price': '$300'}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to MonizTech")

def course(request):
    return HttpResponse("<b>Welcome to MonizTech Course<b/>")

def courseDetails(request, courseid):
    return HttpResponse(courseid)
