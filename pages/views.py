from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request, args, kwargs) #<< Request is an object full of information example request.user
    #return HttpResponse("<h1>Hello world</h1>") #string of html code
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print(request, args, kwargs) #<< Request is an object full of information example request.user
    #return HttpResponse("<h1>Hello world</h1>") #string of html code
    return render(request, "about.html", {
        "myText" : "This is my text",
        "myNumber" : 123,
        "Lest" : [1,2,3,4],
        "daHtml" : "<h1>mio</h1>"

    })

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>") #string of html code