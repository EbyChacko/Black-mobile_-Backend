from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'phone', 'address', 'city', 'state', 'country', 'zip', 'image', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username',
                           'email',
                           'password',
                           'phone',
                           'address',
                           'city',
                           'state',
                           'country',
                           'zip',
                           'image',
                           'is_active',
                           'is_staff',
                           'is_superuser',
                           'date_joined',
                           'updated_at')}),
    )
    list_display = ['username', 'email', 'phone', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)