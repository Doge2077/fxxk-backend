from django.urls import path

from UserCenter import views

urlpatterns = [
    path('loadinfo/', views.loadUserInfo.as_view()),
    path('register/', views.registerUser.as_view()),
]
