from django.http import HttpResponse

# Create your views here.
def faculty_register(request):
    return HttpResponse("<h1> Welcome to faculty registration</h1>")

def faculty_login(request):
    return HttpResponse("<h1> Welcome to faculty login</h1>")

def view_schedule(request):
    return HttpResponse("<h1> Schedules</h1>")

def view_feedback(request):
    return HttpResponse("<h1> View feedback</h1>")

# Create your views here.
