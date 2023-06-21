from django.urls import path
from Analysis import views

urlpatterns = [
    path("loadinfo/", views.loadOneInfo.as_view()),
    path("loadinfos/", views.loadAllInfo.as_view())
]
