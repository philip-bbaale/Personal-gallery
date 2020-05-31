from django.shortcuts import render
from photolibrary.models import Pictures, Category, Location
import random
import os
import pyperclip

# Create your views here.
def pictures_index(request):
    pictures = Pictures.objects.all().order_by('-last_modified')
    view_location = Location.objects.all()
    context = {
        'pictures':pictures,
        'view_locations':view_location
    }
    return render(request, 'pictures.html', context)

def pictures_detail(request, pk):
    picture = Pictures.objects.get(pk=pk)
    view_location = Location.objects.all()
    context = {
        'picture':picture,
        'view_locations':view_location
    }
    return render(request, 'pictures_detail.html', context)

def pictures_category(request, category):
    pictures = Pictures.objects.filter(image_category__category__contains=category).order_by('-created_on')
    view_location = Location.objects.all()
    context = {
        "category": category,
        "pictures": pictures,
        'view_locations':view_location
    }
    return render(request, "pictures_category.html", context)

def pictures_location(request, location):
    pictures = Pictures.objects.filter(image_location__location__contains=location).order_by('-created_on')
    view_location = Location.objects.all()
    context = {
        "location": location,
        "pictures": pictures,
        'view_locations':view_location
    }
    return render(request, "pictures_location.html", context)


def search_results(request):
    view_location = Location.objects.all()

    if 'search_item' in request.GET and request.GET["search_item"]:
        search_term = request.GET.get("search_item")
        searched_pictures = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_pictures": searched_pictures, 'view_locations':view_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message, 'view_locations':view_location})

def copy_image(request, image_url):
    picture_url = image_url
    pyperclip.copy(picture_url)
    pyperclip.paste()
    return render(request, 'pictures_detail.html')

