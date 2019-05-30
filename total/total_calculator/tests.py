from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('total'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Empty View')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')