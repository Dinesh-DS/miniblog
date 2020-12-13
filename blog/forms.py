from django import forms
from blog.models import Post, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'user']
		labels = {'body': 'Description'}


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs = {'class': 'form-control'}),
			'mobile': forms.TextInput(attrs = {'class': 'form-control'}),
			'email': forms.TextInput(attrs = {'class': 'form-control'}),
			'comment': forms.TextInput(attrs = {'class': 'form-control'}),
		}

	def clean_mobile(self):
		mb = str(self.cleaned_data['mobile'])
		if(len(mb) != 10):
			raise forms.ValidationError("Please provide 10 digit mobile number")
		return mb

class SignupForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs = {'class': 'form-control'}))
	password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput(attrs = {'class': 'form-control'}))
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		widgets = {
			'username': forms.TextInput(attrs = {'class': 'form-control'}),
			'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
			'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
			'email': forms.TextInput(attrs = {'class': 'form-control'})
		}

