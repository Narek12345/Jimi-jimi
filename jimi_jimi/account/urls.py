from django.urls import path, include
from django.contrib.auth import urls as auth_urls

app_name = 'account'

urlpatterns = [
	path('', include(auth_urls)),
]