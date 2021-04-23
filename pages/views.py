from django.shortcuts import render
from listings.models import Listing 
from realtors.models import Realtor
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # paginator = Paginator(listings, 6)
    context = {
        "listings": listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all().order_by('-join_date')[:3]
    is_mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "realtors": realtors,
        "is_mvp" : is_mvp
    }
    return render(request, 'pages/about.html', context)
