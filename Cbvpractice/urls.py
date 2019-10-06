from django.contrib import admin
from django.urls import path, include
import crudApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(crudApp.urls)),
]
