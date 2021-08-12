from __future__ import unicode_literals
from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Person


def index(request):
    return HttpResponse("index view...")


def snip_listing(request):
    persons = Person.objects.all()
    return render(request, "listing_pg.html", {"persons": persons})


def snip_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, "detail_pg.html", {"person": person})


def add_new(request):
    f_name = request.POST["first_name"]
    l_name = request.POST["last_name"]
    new_person = Person(first_name=f_name, last_name=l_name)
    new_person.save()
    return render(request, "success_pg.html")
