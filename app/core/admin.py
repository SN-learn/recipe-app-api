"""
Django admin customization.
"""
from django.contrib import admin
# from django.contrib.admin import ModelAdmin as BaseModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    # for displaying list of users
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ("name", "email")
    # for editing a single users
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        (_('Personal Info'), {'fields': ['name', ]}),
        (
            _('Permissions'),
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ]
            }
        ),
        (_('Important dates'), {'fields': ['last_login', ]}),
    ]
    readonly_fields = ['last_login']
    # for adding a new users
    add_fieldsets = [
        (None, {
            'classes': ['wide', ],
            'fields': [
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ],
        }),
    ]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
