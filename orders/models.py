from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE, blank=False)
    is_paid = models.BooleanField(verbose_name=_('Is Paid'), default=False, blank=False, null=False)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=100, blank=False, null=False)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=100, blank=False, null=False)
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), max_length=11, blank=False, null=False, region='IR')
    address = models.CharField(verbose_name=_('Address'), max_length=400, blank=False, null=False)
    notes = models.CharField(verbose_name=_('Order Notes'), max_length=500, blank=True, null=False)
    datetime_created = models.DateTimeField(verbose_name=_("Date of Creation"), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_("Date of Modification"), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('Order of this'), on_delete=models.CASCADE,
                              blank=False, related_name='items')
    product = models.ForeignKey(Product, verbose_name=_('Product of this'), on_delete=models.CASCADE,
                                blank=False, related_name='order_items')
    quantity = models.PositiveIntegerField(verbose_name=_('quantity of this'), default=1, blank=False, null=False)
    price = models.PositiveBigIntegerField(verbose_name=_("price of this"), blank=False, null=False)

    def __str__(self):
        return f'Order Item {self.id}: {self.product} x {self.quantity} (price: {self.price}) of Order {self.order}'

