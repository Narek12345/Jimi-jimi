from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	description = models.TextField()
	file = models.FileField(upload_to="video/%Y/%m/%d/")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)