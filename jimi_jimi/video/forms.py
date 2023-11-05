from django import forms
from .models import Video


class CreateVideoForm(forms.ModelForm):	
	class Meta:
		model = Video
		fields = ['title', 'description', 'file']