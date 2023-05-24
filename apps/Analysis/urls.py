from django.urls import path
from Analysis import views

urlpatterns = [
    path('ans/', views.analysisFiles().as_view())
]
