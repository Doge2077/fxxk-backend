from django.urls import path

from Login import views

urlpatterns = [
    path('register/', views.registerUser.as_view()),
    path('login/', views.loginUser.as_view()),
]
