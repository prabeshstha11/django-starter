from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World!")
    
    people = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "age": 28,
        "occupation": "Data Scientist",
    },
    {
        "id": 2,
        "name": "Marcus Chen",
        "age": 34,
        "occupation": "Graphic Designer",
    },
    {
        "id": 3,
        "name": "Sarah Miller",
        "age": 41,
        "occupation": "Project Manager",
    },
    {
        "id": 4,
        "name": "Leo Rodriguez",
        "age": 25,
        "occupation": "Software Engineer",
    }
]
    
    context = {
        "title": "luffytaro",
        "message": "Welcome to the home page!",
        "people": people
    }
    return render(request, "home.html", context)

def about(request):
    # return HttpResponse("This is the about page.")
    context = {
        "title": "about us",
        "description": "this is about us page and we are django"
    }
    
    return render(request, "about.html", context)

def contact(request):
    context = {
        "title": "contact us",
        "description": "contact use at: 987654321, email us django@gmail.com"
    }
    return render(request, "contact.html", context)