from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     # pass
#     list_display = ["name", "description", "age", "gender"]
#     list_filter = ["age", "gender"]
#     search_fields = ["name"]

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_business", "grade")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        # (
        #     ("Permissions"),
        #     {
        #         "fields": (
        #             "is_active",
        #             "is_staff",
        #             "is_superuser",
        #             "groups",
        #             "user_permissions",
        #         ),
        #     },
        # ),
    )
    # pass
