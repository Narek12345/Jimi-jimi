from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(length=150)
	description = models.TextField()
	public_data = models.DateTimeField(auto_now_add=True)
