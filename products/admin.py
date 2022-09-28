from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'star', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created', ]

    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'star', 'datetime_created', 'active', ]
