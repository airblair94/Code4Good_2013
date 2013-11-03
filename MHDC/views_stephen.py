from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import auth
from models import *
from forms import *
import datetime


#Allows for viewing a list of all in-progress apps associated with a user
#url: /user_app
def view_my_applications(request):
	user = request.user
	if user.is_authenticated():
		user_profile = user.get_profile()
		apps = SelfHelpApplication.objects.filter(userProfile=user_profile).exclude(status="Completed")
		output = "<h2>Self Help Applications</h2><br><ul>"
		for app in apps:
			output += '<li><a href="/self_help_app/'+str(app.id)+'"> Application ' + str(app.id) + " edited on: " + str(app.dateReceived) + "</a></li>"
		output += "</ul><br><h2>Home Repair Applications</h2><br><ul>"
		apps = HomeRepair.objects.filter(id=user_profile.user_id)
		for app in apps:
			output += '<li><a href="/home_repair_app/'+str(app.id)+'"> Application ' + str(app.id) + " edited on: " + str(app.dateReceived) + "</a></li>"
		return render(request, "user.html", {"content":output})
	else:
		return HttpResponse("Please log in to view applications")

#Allows for viewing a list of all completed apps associated with a user
#url: /comp_app
def view_completed_applications(request):
	user = request.user
	if user.is_authenticated():
		user_profile = user.get_profile()
		apps = SelfHelpApplication.objects.filter(userProfile=user_profile, status="Completed")
		output = "<h2>Completed Self Help Applications</h2><br><ul>"
		for app in apps:
			output += '<li><a href="/self_help_app/'+str(app.id)+'"> Application ' + str(app.id) + " edited on: " + str(app.dateReceived) + "</a></li>"
		output += "</ul><br><h2>Completed Home Repair Applications</h2><br><ul>"
		apps = HomeRepair.objects.filter(id=user_profile.user_id)
		for app in apps:
			output += '<li><a href="/home_repair_app/'+str(app.id)+'"> Application ' + str(app.id) + " edited on: " + str(app.dateReceived) + "</a></li>"
		return render(request, "user.html", {"content":output})
	else:
		return HttpResponse("Please log in to view applications")

#Allows for viewing and editing of self help forms
#url: /self_help_app/id
def self_help_view(request, app_id):
	user = request.user
	if user.is_authenticated():
 		if user.groups.filter(name="staff"):
			app = SelfHelpApplication.objects.filter(id=app_id)
			user_profile = app[0].userProfile
			sidebar = "staff_sidebar.html"
		else:
			user_profile = user.get_profile()
			app = SelfHelpApplication.objects.filter(id=app_id, userProfile=user_profile)
			sidebar = "user_sidebar.html"
		if len(app) == 0:
				return HttpResponse("You don't have the permissions to view this application")
		else:
			app = app[0]
		if request.method == "POST":
			if app.status == "Completed":
				return HttpResponse("Application is completed, cannot edit.")
			else:
				form = SelfHelpForm(data=request.POST, instance=app)
				if form.is_valid():
					form.userProfile = user_profile
					new_app = form.save()
					setattr(new_app, "dateReceived", datetime.datetime.now().strftime("%m/%d/%Y"))
					new_app.save()
					return HttpResponse("Success!")
		else:
			form = SelfHelpForm(instance=app)
			return render(request, "edit_form.html", {"form":form, "action":"/self_help_app/"+str(app_id), "sidebar":sidebar})
	else:
		return HttpResponse("Please log in to view applications")

#Allows for viewing and editing of home repair forms
#url: /home_repair_app/id
def home_repair_view(request, app_id):
	user = request.user
	if user.is_authenticated():
		if user.groups.filter(name="staff"):
			app = HomeRepair.objects.filter(id=app_id)
			user_profile = app[0].userProfile
			sidebar = "staff_sidebar.html"
		else:
			user_profile = user.get_profile()
			app = HomeRepair.objects.filter(id=app_id, userProfile=user_profile)
			sidebar = "user_sidebar.html"
		if len(app) == 0:
				return HttpResponse("You don't have the permissions to view this application")
		else:
			app = app[0]
		if request.method == "POST":
			if app.status == "Completed":
				return HttpResponse("Application is completed, cannot edit.")
			else:
				form = HomeRepairForm(data=request.POST, instance=app)
				if form.is_valid():
					form.userProfile = user_profile
					new_app = form.save()
					setattr(new_app, "dateReceived", datetime.datetime.now().strftime("%m/%d/%Y"))
					new_app.save()
					return HttpResponse("Success!")
		else:
			form = HomeRepairForm(instance=app)
			return render(request, "edit_form.html", {"form":form, "action":"/home_repair_app/"+str(app_id), "sidebar":sidebar})
	else:
		return HttpResponse("Please log in to view applications")

def account_info_view(request):
	user = request.user
	if user.is_authenticated():
		user_profile = user.get_profile()
		if user.groups.filter(name="staff"):
			sidebar = "staff_sidebar.html"
		else:
			sidebar = "user_sidebar.html"
		if request.method == "POST":
			form = UserProfileForm(data=request.POST, instance=user_profile)
			if form.is_valid():
				#form.userProfile = user_profile
				new_app = form.save()
				#setattr(new_app, "dateReceived", datetime.datetime.now().strftime("%m/%d/%Y"))
				#new_app.save()
				return HttpResponse("Success!")
		else:
			form = UserProfileForm(instance=user_profile)
			return render(request, "edit_form.html", {"form":form, "action":"/account_info", "sidebar":sidebar})
	else:
		return HttpResponse("Please log in to view applications")
