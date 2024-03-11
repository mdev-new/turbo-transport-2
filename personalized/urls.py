from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('last_searches', views.last_searches, name='last_searches'),
    path('session_controls', views.session_controls, name='session_controls')
]
