from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

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

    def test_password_reset_load(self):
        response = self.client.get('/accounts/password/reset/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('account_reset_password'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_contain(self):
        response = self.client.get(reverse('account_reset_password'))
        self.assertContains(response, 'Password Reset')

    def test_password_reset_POST(self):
        response = self.client.post(reverse('account_reset_password'),
                                    {
                                        'email': 'test@gmail.com'
                                    })
        self.assertEqual(response.status_code, 302)

    def test_authentication_POST(self):
        # checking user is not login
        response = self.client.get(reverse('account_login'))
        self.assertNotEqual(response.status_code, 302)
        response = self.client.get(reverse('account_signup'))
        self.assertNotEqual(response.status_code, 302)

        # signup POST
        response = self.client.post(reverse('account_signup'),
                                    {
                                        'email': 'nuser@gmail.com',
                                        'password1': 'nuser1pass',
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.last().email, 'nuser@gmail.com')

        # logout load
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 200)

        # logout contain
        response = self.client.get(reverse('account_logout'))
        self.assertContains(response, 'LOGOUT')

        # logout POST
        response = self.client.post(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)

        # login POST
        response = self.client.post(reverse('account_login'),
                                    {
                                            'login': 'nuser@gmail.com',
                                            'password': 'nuser1pass',
                                    })
        self.assertEqual(response.status_code, 302)

        # password change load
        response = self.client.get('/accounts/password/change/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('account_change_password'))
        self.assertEqual(response.status_code, 200)

        # password change contain
        response = self.client.get(reverse('account_change_password'))
        self.assertContains(response, 'Change Password')

        # password change POST
        response = self.client.post(reverse('account_change_password'),
                                    {
                                        'oldpassword': 'nuser1pass',
                                        'password1': 'newpass1user',
                                        'password2': 'newpass1user'
                                    })
        self.assertEqual(response.status_code, 302)
