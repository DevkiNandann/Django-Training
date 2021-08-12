from django.test import SimpleTestCase
from django.urls import reverse, resolve
from snippets.views import snip_listing, snip_detail, add_new


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse("snippets:list")
        print(resolve(url))
        self.assertEquals(resolve(url).func, snip_listing)

    def test_detail_url_is_resolved(self):
        url = reverse("snippets:detail", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, snip_detail)

    def test_addnew_url_is_resolved(self):
        url = reverse("snippets:addnew")
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_new)
