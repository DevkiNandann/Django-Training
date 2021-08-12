from selenium import webdriver
from snippets.models import Person
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

        list_url = self.live_server_url + reverse("snippets:list")
        self.assertEquals(self.browser.current_url, list_url)

    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)

        add_url = self.live_server_url + reverse("snippets:addnew")
        self.assertEquals(self.browser.current_url, add_url)

    def test_user_is_redirected_to_project_detail(self):
        p = Person.objects.create(first_name="Dn", last_name="G")
        self.browser.get(self.live_server_url)

        detail_url = self.live_server_url + reverse("snippets:detail", args=[p.id])
        self.assertEquals(self.browser.current_url, self.live_server_url + "/")
