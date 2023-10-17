from django.shortcuts import render
from .models import Video
from .forms import CreateVideoForm


def add_video(request):
	if request.method == 'POST':
		form = CreateVideoForm(request.POST, request.FILES)
		if form.is_valid():
			new_video = form.save(commit=False)
			new_video.user = request.user
			new_video.url = 'https://github.com/'
			new_video.save()
	else:
		form = CreateVideoForm()
	return render(request, 'video/add_video.html', {'form': form})