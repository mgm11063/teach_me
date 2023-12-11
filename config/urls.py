from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/answers/", include("answers.urls")),
    path("api/v1/questions/", include("questions.urls")),
]
