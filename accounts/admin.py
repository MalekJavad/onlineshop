from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeFrom


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeFrom
    add_form = CustomUserCreationForm
    list_display = ['username', 'email', ]
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('age', )}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('age', )}),
    # )



