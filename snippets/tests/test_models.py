from django.test import TestCase
from snippets.models import Person


class TestModels(TestCase):
    def setUp(self):
        self.person = Person.objects.create(first_name="A", last_name="P")

    def test_person(self):
        self.assertEquals(self.person.first_name, "A")
