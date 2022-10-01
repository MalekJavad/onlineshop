from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Product Title'))
    description = RichTextField(verbose_name=_('Product Description'))
    short_description = models.TextField(blank=True, verbose_name=_('Product Short Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Product Price'))
    active = models.BooleanField(default=True, verbose_name=_('Product Active Status'))
    image = models.ImageField(upload_to='products/product_cover/', verbose_name=_('Product Image'), blank=True)

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('Date Time of Creation'))
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Comment(models.Model):

    PRODUCT_STAR_CHOICES = (
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect')),
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Comment Author')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Product of Comment')
    )

    body = models.TextField(verbose_name=_('comment text'))
    star = models.CharField(max_length=10, choices=PRODUCT_STAR_CHOICES, verbose_name=_('score'))

    active = models.BooleanField(default=True, verbose_name=_('Comment Active Status'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # manager
    object = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
