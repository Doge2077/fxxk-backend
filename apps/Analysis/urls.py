from django.urls import path
from Analysis import views

urlpatterns = [
    path("loadallinfo/", views.loadAllInfo.as_view()),
    path("loadonejob/", views.loadOneJob.as_view()),
    path("loadalljob/", views.loadAllJob.as_view())
]
