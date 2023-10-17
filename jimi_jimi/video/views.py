from django.shortcuts import render
from .models import Video
from .forms import CreateVideoForm


def add_video(request):
	if request.method == 'POST':
		form = CreateVideoForm(data=(request.POST, request.FILES))
		if form.is_valid():
			data = form.cleaned_data
			print(data)
	else:
		form = CreateVideoForm()