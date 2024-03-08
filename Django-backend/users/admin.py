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
    model = User
    list_display = ("pk", "username", "email", "is_business", "grade")
    list_display_links = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("email", "grade", "is_business")},
         ),
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
