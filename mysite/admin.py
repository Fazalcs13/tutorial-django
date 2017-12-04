from django.contrib import admin
from .models import CreateUser, AddCourses, CoursesTopic

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_author_name', 'course_duration', 'course_date', 'course_category')
    list_filter = ('course_title', 'course_author_name', 'course_duration', 'course_date', 'course_category')
    search_fields = ('course_title', 'course_category')

admin.site.register(AddCourses, CourseAdmin)
admin.site.register(CoursesTopic)
