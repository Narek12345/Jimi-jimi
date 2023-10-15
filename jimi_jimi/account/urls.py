from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from . import views

app_name = 'account'

urlpatterns = [
	path('dashboard/', views.dashboard, name='dashboard'),
	path('', include(auth_urls)),
]