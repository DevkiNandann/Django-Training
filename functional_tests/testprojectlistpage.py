from selenium import webdriver
from snippets.models import Person
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

        # user request the page for first time
        alert = self.browser.find_element_by_class_name("noproject-wrapper")
        self.assertEquals(alert.find_element_by_tag_name("h3").text, "Sorry")

    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)

        # user request the page for first time
        add_url = self.live_server_url + reverse("snippets/info/add-name")
        self.browser.find_element_by_class_name("a").click()
        self.assertEquals(self.browser.current_url, add_url)

    def test_user_sees_project_list(self):
        p = Person.objects.create(first_name="Dn", last_name="G")
        self.browser.get(self.live_server_url)

        # user request the page for first time
        self.assertEquals(self.browser.find_element_by_tag_name("h5").text, "p")

    def test_user_is_redirected_to_project_detail(self):
        p = Person.objects.create(first_name="Dn", last_name="G")
        self.browser.get(self.live_server_url)
        time.sleep(10)

        # user sees the project on the screen. He clicks the VISIT link as is
        # redirected to the detail page
        detail_url = self.live_server_url + reverse("detail", args=[p.slug])
        self.browser.find_element_by_link_text("VISIT").click()
        self.assertEquals(self.browser.current_url, detail_url)
