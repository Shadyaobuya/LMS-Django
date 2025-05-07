from django.contrib import admin

# Register your models here.

from lms_auth.models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_student', 'is_admin')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    ordering = ('username',)