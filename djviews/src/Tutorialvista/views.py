from django.http import HttpResponse
from django.shortcuts import render
from src.listings.models import Listing
from src.realtors.models import Realtor
# Create your views here.

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {
		'listings':listings
	}
	return render(request,r'pages\index.html',context)


def about(request):
	# get all realtors
	realtors = Realtor.objects.order_by('-hire_date')
	#get mvp
	mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
	context ={
		'realtors':realtors,
		'mvp_realtor':mvp_realtor
	}
	return render(request,r'pages\about.html',context)