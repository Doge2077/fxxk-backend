from django.urls import path

from UserCenter import views

urlpatterns = [
    path('loadinfo/', views.loadUserInfo.as_view()),
    path('addworkneed/', views.addWorkNeed.as_view()),
]
