from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	detail = models.TextField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.id})
