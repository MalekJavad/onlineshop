from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Product, Comment

# Create your tests here.


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Product.objects.create(
            title='test-title',
            description='test-description',
            price=26000,
            active=True,
        )

    def test_list_page_load(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_page_contain(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, 'test-title')

    def test_detail_page_load(self):
        response = self.client.get(f'/products/{self.post.id}')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('product_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_contain(self):
        response = self.client.get(reverse('product_detail', args=[self.post.id]))
        self.assertContains(response, 'test-description')

    def test_detail_page_comment_POST_and_GETform(self):
        # signup and login a test user for posting Comment
        response = self.client.post(reverse('account_signup'),
                                    {
                                        'email': 'test@gmail.com',
                                        'password1': 'test1user',
                                    })
        self.assertEqual(response.status_code, 302)

        # posting the Comment
        response = self.client.post(reverse('comment_create', args=[self.post.id]),
                                    {
                                        'body': 'this-is-tset',
                                        'star': '1',
                                    })
        self.assertEqual(response.status_code, 302)

        # checking if the Comment is shown
        response = self.client.get(reverse('product_detail', args=[self.post.id]))
        self.assertContains(response, 'this-is-tset')
