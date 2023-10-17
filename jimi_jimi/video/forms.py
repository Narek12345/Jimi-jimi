from django import forms
from .models import Video


class CreateVideoForm(forms.ModelForm):
	file = forms.FileField()
	
	class Meta:
		model = Video
		fields = ['title', 'description']