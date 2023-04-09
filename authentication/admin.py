from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from authentication.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email', 'team')
    list_filter = ('team',)
    search_fields = ('username', 'last_name', 'first_name', 'email')

    fieldsets = (
        (None, {"fields": ("username", "password", "team")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "team"),
            },
        ),
    )


admin.site.register(User, UserAdmin)
