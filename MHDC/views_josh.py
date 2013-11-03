from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *

import datetime

def analysis(request):
	users = UserProfile.objects.all()
	homeRepair = HomeRepair.objects.all()
	selfHelp = SelfHelpApplication.objects.all()

	#Total number of users
	count = users.count()

	#Number and percent of Completed Apps
	homeRepairComplete = homeRepair.filter(status="Complete").count()
	selfHelpComplete = selfHelp.filter(status="Complete").count()
	finished = homeRepairComplete + selfHelpComplete 
	percentHomeRepair = calcPercent(homeRepairComplete, homeRepair.count())
	percentSelfHelp = calcPercent(selfHelpComplete, selfHelp.count())
	percentComplete = calcPercent(finished, count)
	percentIncomplete = 100 - percentComplete 

	#Number and percent of disabled users
	disabled = users.filter(disability=True)
	disabledCount = disabled.count()
	percentDisabled = calcPercent(disabledCount, count) 

	#Number and percent of veteran users
	veterans = users.filter(veteran=True).count()
	percentVeteran = calcPercent(veterans, count)
	
	#Age Demographics
	currentYear = datetime.datetime.now().year
	under25 = users.filter(DOB__gt=datetime.date(currentYear-25, 1, 1))
	under25 = under25.count()
	under25 = calcPercent(under25, count) 
	under40 = users.filter(DOB__gt=datetime.date(currentYear-40, 1, 1)).exclude(DOB__gt=datetime.date(currentYear-25,1,1))
	under40 = under40.count()
	under40 = calcPercent(under40, count) 
	under65 = users.filter(DOB__gt=datetime.date(currentYear-65, 1,1)).exclude(DOB__gt=datetime.date(currentYear-40,1,1))
	under65 = under65.count()
	under65 = calcPercent(under65, count) 
	over65 = users.exclude(DOB__gt=datetime.date(currentYear-65, 1, 1))
	over65 = over65.count()
	over65 = calcPercent(over65, count) 
	ageDemos = {"under25":under25, "under40":under40, "under65":under65, "over65":over65}

	#Race Demographics
	w = users.filter(race = "w").count()
	w = calcPercent(w, count)
	b = users.filter(race = "b").count()
	b = calcPercent(b, count)
	h = users.filter(race = "h").count()
	h = calcPercent(h, count)
	o = users.filter(race = "o").count()
	o = calcPercent(o, count)
	raceDemos = {"w":w, "b":b, "h":h, "o":o}
	
	#Averages
	totalAge = 0
	totalIncome = 0
	for i in range(0, count, 1):
		birthYear = users[i].DOB.year
		age = currentYear - birthYear
		totalAge += age
	if(count == 0):
		avgAge = 0
	else:
		avgAge = totalAge/count

	stats = {"count":count, "percentDisabled":percentDisabled, "percentVeteran":percentVeteran, "ageDemos":ageDemos, "raceDemos":raceDemos, "avgAge":avgAge}
	return render(request, "../templates/stats.html", {"stats": stats})

#Simple function to calculate %
def calcPercent(value, total):
	if(total == 0):
		return 0
	print("total: {0}, value: {1}".format(total, value))
	return (float(value)/float(total)) * 100.0
