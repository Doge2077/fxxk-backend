from django.urls import path
from Analysis import views

urlpatterns = [
    path("loadallinfo/", views.loadAllInfo.as_view()),
    path("loadnameinfo/", views.loadNameInfo.as_view()),
    path("loadonejob/", views.loadOneJob.as_view()),
    path("loadalljob/", views.loadAllJob.as_view()),
    path("loadidinfo/", views.loadIdInfo.as_view()),
    path("loadscore/", views.loadScore.as_view())
]
