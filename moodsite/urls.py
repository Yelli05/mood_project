from django.contrib import admin
from django.urls import path, include
from moods.views import mood_home  # 👈 import mood homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mood_home, name="mood_home"),  # 👈 set mood_home as homepage
    path("foodpicker/", include("foodpicker.urls")),
    
]
