from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *
from views import *
from django.contrib.auth.models import Group

def user_login(request):
	if request.method == "POST":
		print request.POST
		username = request.POST.get("email_address", "")
		password = request.POST.get("password", "")
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponse("Logged in!<div class=\"successIndicator\"></div>")
		form_errors = True
	return render(request, "login_form.html", {"form_errors":form_errors})

def register_user(request):
	form = [UserForm(request.POST or None), UserProfileForm(request.POST or None)]
	if form[0].is_valid() and form[1].is_valid():
		new_user = form[0].save(commit = False)
		new_user.username = new_user.email
		new_user = form[0].save()
		g = Group.objects.get(name='client') 
		g.user_set.add(new_user)
		profile = form[1].save(commit = False)
		profile.user = new_user
		profile.save()
		
		#Log the user in:
		new_user = auth.authenticate(username = new_user.email, password = request.POST["password"])
		auth.login(request, new_user)
		return HttpResponse("Registration Successful!")
	return render(request, "user_registration_form.html", {"user_form":form[0], "profile_form":form[1]})

def user_logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")
