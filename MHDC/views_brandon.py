from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from models import *

def home_repairs(request):
	return HttpResponse("Hello")

def self_help(request):
	return HttpResponse("Hello")
