from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('assignments/', include('core.assignments.urls')),
    path('graded-assignments/', include('core.graded_assignments.urls')),
    path('users/', include('users.urls')),
]
