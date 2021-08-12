from __future__ import unicode_literals
from django.http.response import HttpResponse
from snippets.serializers import PersonSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins

from .models import Person


def index(request):
    return HttpResponse("index view...")


class SnippetList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(APIView):
    """
    Get the detail of a person with id
    """

    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
