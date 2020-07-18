
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sms/', include('school_app.urls')),
    path('registered-students/', include('students.urls')),
    path('registered-courses/', include('courses.urls')),
    path('accounts/login', include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
