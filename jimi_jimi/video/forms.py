from django import forms
from .models import Video


class CreateVideoForm(form.ModelForm):
	class Meta:
		model = Video
		fields = ['title', 'description']