from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('logged_in', views.success),
    path('check_log', views.check_login),
]
