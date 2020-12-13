from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICE = (('draft', 'Draft'), ('publish','Publish')) 

class Post(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	body = models.TextField()
	published_date = models.DateField(auto_now_add=True)
	updated_date = models.DateField(auto_now=True)
	blog_status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='draft')


class Contact(models.Model):
	name = models.CharField(max_length=100)
	mobile = models.IntegerField()
	email = models.EmailField()
	comment = models.TextField(blank=True)

	def __str__(self):
		return self.name