from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,"home.html",{})
	#return HttpResponse("HELLO MADAFAKA")

def about(request):
	return render(request,"about.html",{})

def contact(request):
	return render(request,"contact.html",{})
