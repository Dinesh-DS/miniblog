from django.shortcuts import render
from blog.models import Post
from blog.forms import PostForm, ContactForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.


def home(request):
	posts = Post.objects.filter(blog_status='publish').order_by('-id')
	return render(request, 'blog/home.html', {'posts': posts})

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	return render(request, 'blog/contact.html', {'form':form})

def post_detail(request, id):
	post = Post.objects.get(pk=id)
	return render(request, 'blog/detail.html', {'post':post})

def add_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile/')
	return render(request, 'blog/add.html', {'form': form})

def user_profile(request):
	if request.user.is_authenticated:
		posts = Post.objects.filter(user__username=request.user)
		return render(request, 'blog/profile.html', {'posts':posts})
	else:
		return HttpResponseRedirect('/login/')

def update_post(request, id):
	post = Post.objects.get(pk=id)
	form = PostForm(instance=post)
	if  request.method == 'POST':
		post = Post.objects.get(pk=id)
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile/')
	return render(request, 'blog/add.html', {'form':form})

def delete_post(request, id):
	post = Post.objects.get(pk=id)
	post.delete()
	return HttpResponseRedirect('/profile/')

def signup_view(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='author')
			user.groups.add(group)
			form = SignupForm()
	return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
	if not request.user.is_authenticated:
		form = AuthenticationForm(request=request)
		if request.method == 'POST':
			form = AuthenticationForm(request=request, data=request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				pwd = form.cleaned_data['password']
				user = authenticate(username=uname, password=pwd)
				if user != None:
					login(request, user)
					return HttpResponseRedirect('/profile/')
		return render(request, 'blog/login.html', {'form': form})
	else:
		return HttpResponseRedirect('/profile/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
