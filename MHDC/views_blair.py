
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *

def homepage(request):
		user = request.user
		if user.is_authenticated():
				if user.groups.filter(name="staff"):
						sidebar_var="staff_sidebar.html"
				else: #user.groups.filter(name="client"):
						sidebar_var="user_sidebar.html"
		else:
				sidebar_var="login_form.html"
		return render(request, "general_welcome.html", {"sidebar_var":sidebar_var})

def general_welcome(request):
	pass
def search(request):
	user = request.user
	sidebar_var = "staff_sidebar.html"
	l = []
	for i in User.objects.all():
		if i.groups.filter(name="client"):
			l.append(i)	
	return render(request, "search.html", {"content":l, "sidebar_var":sidebar_var})
