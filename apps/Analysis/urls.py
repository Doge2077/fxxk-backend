from django.urls import path
from Analysis import views

urlpatterns = [
    path("loadallinfo/", views.loadAllInfo.as_view()),
]
