import requests
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Video
from .forms import CreateVideoForm


def video_list(request):
	return render(request, 'video/video_list.html', {})


@ensure_csrf_cookie
def add_video(request):
	if request.method == 'POST':
		form = CreateVideoForm(request.POST, request.FILES)
		if form.is_valid():
			# Take the transferred file.
			file = request.FILES['file']

			# Create new video.
			new_video = form.save(commit=False)
			new_video.user = request.user

			# Save new video.
			new_video.save()
	else:
		form = CreateVideoForm()
	return render(request, 'video/add_video.html', {'form': form})