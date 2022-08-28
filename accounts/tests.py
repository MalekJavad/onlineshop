from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class AccountsTest(TestCase):
    def test_login_load(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_login_contain(self):
        response = self.client.get(reverse('account_login'))
        self.assertContains(response, 'LOGIN')

    def test_signup_load(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_contain(self):
        response = self.client.get(reverse('account_signup'))
        self.assertContains(response, 'Signup')

    # def test_logout_load(self):
    #     response = self.client.get('/accounts/logout/')
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.get(reverse('account_logout'))
    #     self.assertEqual(response.status_code, 200)

    # def test_logout_contain(self):
    #     response = self.client.get(reverse('account_logout'))
    #     self.assertContains(response, 'LOGOUT')
