from django.test import TestCase, Client
from django.urls import reverse
from snippets.models import Person


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("snippets:list")
        self.person = Person.objects.create(first_name="A", last_name="P")
        self.detail_url = reverse("snippets:detail", args=[self.person.id])
        self.add_new_url = reverse("snippets:addnew")

    def test_snip_listing_GET(self):
        resp = self.client.get(self.list_url)

        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "listing_pg.html")

    def test_snip_detail_GET(self):
        resp = self.client.get(self.detail_url)

        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "detail_pg.html")

    def test_add_new_POST(self):

        resp = self.client.post(
            self.add_new_url,
            {
                "first_name": "Tanmaya",
                "last_name": "Sharma",
            },
        )

        p2 = Person.objects.get(first_name="Tanmaya")

        self.assertEquals(p2.first_name, "Tanmaya")
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "success_pg.html")
