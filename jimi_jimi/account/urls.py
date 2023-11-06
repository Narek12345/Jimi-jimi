from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
	path('register/', views.register, name='register'),
	path('logout/', views.logout, name='logout'),
	path('', include('django.contrib.auth.urls')),
	path('', views.profile, name='profile'),
]