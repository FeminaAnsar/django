from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def stud_register(request):
    return render(request, "student/studlogin.html")

def registration(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    course=request.POST.get("crse")
    print(name,course,email)
    return render(request, "student/studlogin.html")


def stud_login(request):
    return HttpResponse("<h1> Welcome to student login</h1>")

def view_timetable(request):
    return HttpResponse("<h1> Timing</h1>")

def post_feedback(request):
    return HttpResponse("<h1> Post your feedback</h1>")