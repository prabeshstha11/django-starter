from django.shortcuts import render, redirect
from .models import Receipe

# Create your views here.
def receipe_list(request):
    receipe = Receipe.objects.all()
    context = {
        "title": "Receipe Book",
        "receipes": receipe
    }
    return render(request, "list.html", context)


def create_list(request):
    if request.method == "POST":
        name = request.POST.get("title")
        description = request.POST.get("description")
        ingredients = request.POST.get("ingredients")
        time = request.POST.get("time")
        level = request.POST.get("level")
    
        Receipe.objects.create(name=name, description=description, ingredients=ingredients, time=time, level=level)
        
        return redirect("/receipe/")

    return render(request, "create.html")

def update_list(request, id):
    receipe = Receipe.objects.get(id = id)
    context = {
        "receipe": receipe
    }
    
    if request.method == "POST":
        name = request.POST.get("title")
        description = request.POST.get("description")
        ingredients = request.POST.get("ingredients")
        time = request.POST.get("time")
        level = request.POST.get("level")
    
        # Receipe.objects.create(name=name, description=description, ingredients=ingredients, time=time, level=level)
        receipe.name = name
        receipe.description = description
        receipe.ingredients = ingredients
        receipe.time = time
        receipe.level = level
        receipe.save()
        
        return redirect("/receipe/")

    return render(request, "update.html", context=context)


def delete_item(request, id):
    receipe = Receipe.objects.get(id = id)
    receipe.delete()
    
    return redirect("/receipe/")
