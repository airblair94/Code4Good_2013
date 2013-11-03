from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *
from forms import *

#IN PROGRESS: ---------------------
def get_document_checklist(request):
	u = request.user
	if u.is_authenticated():
        	checklist = []
        	for i in DocCheckList.objects.filter(userProfile=u.get_profile()):
        		checklist.append(i)
    		if len(checklist) > 0:
			print "yes"
        	return render(request, "self_help_client_check.html", {"content":checklist})
	else:
		return HttpResponse("Please log in")
def get_self_help_staff_checklist(request):
    u = request.user
    checklist = SelfHelpStaffChecklist.objects.filter(user=u)
    return render(request, "index.html", {"content":checklist})

def get_repair_checklist(request):
    u = request.user
    checklist = RepairChecklist.objects.filter(user=u)
    return render(request, "index.html", {"content":checklist})

def get_repair_internal_checklist(request):
    u = request.user
    checklist = RepairInternalChecklist.objects.filter(user=u)
    return render(request, "index.html", {"content":checklist})
