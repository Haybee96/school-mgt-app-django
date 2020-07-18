from django.contrib import admin
from . models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'phone', 'level', 'created')
    list_display_links = ('id', 'firstname')
    list_per_page = 10
    list_filter = ('level',)
    search_fields = ('firstname', 'lastname', 'email', 'phone', 'level')

admin.site.register(Student, StudentAdmin)
