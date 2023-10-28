from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
	path('add_video/', views.add_video, name='add_video'),
	path('', views.video_list, name='video_list'),
]