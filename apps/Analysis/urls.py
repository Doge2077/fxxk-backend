from django.urls import path
from Analysis import views

urlpatterns = [
    path("loadinfo/", views.loadInfo.as_view())
]
