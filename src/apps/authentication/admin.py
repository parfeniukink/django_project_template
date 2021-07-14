from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password", "last_login")
    exclude = ("user_permissions", "groups")
