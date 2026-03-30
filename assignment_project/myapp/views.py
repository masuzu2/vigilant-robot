from django.shortcuts import render, redirect
from myapp.models import Person

def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(name=name, age=age)
        person.save()
        return redirect("/")
    else:
        return render(request, "form.html")
