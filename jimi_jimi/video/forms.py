from django import forms
from .models import Video


class CreateVideoForm(form.ModelForm):
	file = forms.FileField()
	
	class Meta:
		model = Video
		fields = ['title', 'description']