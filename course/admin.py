from django.contrib import admin

# Register your models here.
from course.models import Course, Topic, Assignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    list_filter = ("created_at",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    search_fields = ("name",)
    list_filter = ("created_at",)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "assignment_topic")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
