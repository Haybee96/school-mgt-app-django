from django.contrib import admin
from . models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code', 'unit', 'created')
    list_display_links = ('title',)
    list_per_page = 10
    list_filter = ('unit',)
    search_fields = ('title', 'code', 'unit')

admin.site.register(Course, CourseAdmin)