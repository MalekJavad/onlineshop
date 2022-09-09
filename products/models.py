from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
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
        verbose_name='comment author'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    body = models.TextField(verbose_name=_('comment text'))
    star = models.CharField(max_length=10, choices=PRODUCT_STAR_CHOICES, verbose_name=_('score'))

    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # manager
    object = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
