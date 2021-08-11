# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse

from django.shortcuts import render

from .models import Products, Person

def index(request):
    return HttpResponse('index view...')



def snip_listing(request):
    persons = Person.objects.all()
    return render(request, 'listing_pg.html', {'persons': persons})


def snip_detail(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'detail_pg.html', {'person': person})
    

def add_new(request):
    f_name = request.GET['first_name']
    l_name = request.GET['last_name']
    new_person = Person(first_name=f_name, last_name=l_name)
    new_person.save()
    return HttpResponse(f'Person {new_person} successfully added')