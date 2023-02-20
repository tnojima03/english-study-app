from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User
from mysite.forms import UserCreationForm
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
 
    #to create users in admin
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    #to create users in admin
    add_form = UserCreationForm
 
 
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)