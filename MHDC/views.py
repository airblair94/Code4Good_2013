from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *
from forms import *

import datetime

#Finished -------
def self_help_application(request):
	u = request.user
	if u.is_authenticated():
		if request.method == "POST":
			form = SelfHelpForm(data=request.POST)
			if form.is_valid():
				new_app = form.save(commit=False)
				setattr(new_app, "userProfile", u.get_profile())
				setattr(new_app, "dateReceived", datetime.datetime.now().strftime("%m/%d/%Y"))
				new_app.save()
				return HttpResponse("Application Submitted!")
		else:
			form = SelfHelpForm()
	else:
		return HttpResponse("Please log in to submit an application.")
	return render(request, "self_help_form.html", {"form":form})

def new_application(request):
	sidebar_var="user_sidebar.html"
	return render(request, "new_app.html", {"sidebar_var":sidebar_var})

def home_repair_application(request):
	u = request.user
	if u.is_authenticated():
		if request.method == "POST":
			form = HomeRepairForm(data=request.POST)
			if form.is_valid():
				new_app = form.save(commit=False)
				setattr(new_app, "userProfile", u.get_profile())
				setattr(new_app, "dateReceived", datetime.datetime.now().strftime("%m/%d/%Y"))
				new_app.save()
				return HttpResponse("Application Submitted!")
		else:
			form = HomeRepairForm()
	else:
		return HttpResponse("Please log in to submit an application.")
	return render(request, "home_repair_form.html", {"form":form})


#def new_member_application(request):
#	if request.method == "POST":
#        	form = UserProfileForm(data=request.POST)
#                if form.is_valid():
#                	form.save()
#	else:
#                form = UserProfileForm()
#        return render(request, "new_member.html", {"form":form})

#IN PROGRESS: ---------------------
