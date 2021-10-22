from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from github_oauth.custom_user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    pass
