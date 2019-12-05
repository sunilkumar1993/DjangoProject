from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

from .models import Listing
# Create your views here.
def  listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        'listings':paged_listings
    }

    return render(request,r'listings\listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing' : listing
    }
    return render(request,r'listings\listing.html',context)

def search(request):
    return render(request,r'listings\search.html')