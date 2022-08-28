from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class PageTest(TestCase):
    def test_homepage_load(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_contain(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_aboutus_load(self):
        response = self.client.get('/about-us')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('about-us'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_contain(self):
        response = self.client.get(reverse('about-us'))
        self.assertContains(response, 'This is About Us page mate!')
