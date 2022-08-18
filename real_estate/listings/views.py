from multiprocessing import context
from django.shortcuts import render
from .models import Listing
from .forms import ListingForm

# Create your views here.

# CRUD - Create, retrieve, update, delete, list


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)