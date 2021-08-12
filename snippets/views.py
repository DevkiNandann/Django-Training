from __future__ import unicode_literals
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from snippets.serializers import PersonSerializer

from django.shortcuts import render, get_object_or_404

from .models import Person


def index(request):
    return HttpResponse("index view...")


@csrf_exempt
def snip_listing(request):
    persons = Person.objects.all()
    return render(request, "listing_pg.html", {"persons": persons})
    # serializer = PersonSerializer(persons, many=True)
    # return JsonResponse(serializer.data, safe=False)


def snip_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, "detail_pg.html", {"person": person})


@csrf_exempt
def add_new(request):
    # f_name = request.POST["first_name"]
    # l_name = request.POST["last_name"]
    # new_person = Person(first_name=f_name, last_name=l_name)
    # new_person.save()
    # return render(request, "success_pg.html")
    data = request.POST
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
