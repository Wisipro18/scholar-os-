from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # core app (dashboard, etc)
    path('', include('core.urls')),

    # accounts WITHOUT prefix
    path('', include('accounts.urls')),
]