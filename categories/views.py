from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from genres.models import Genre
from drink_categories.models import DrinkCategory

def category(request, slug_category):
    #handles display of events belonging to a single category
    category = Category.objects.filter(slug=slug_category) #slugify url
    if category.exists():
        category = category.first()
    else:
        raise Http404
    category_name = Category.objects.get(slug=slug_category)
    cover_image = Event.objects.order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='') #display all cover images in detailed category
    events = Event.objects.order_by('event_date').filter(categories__slug=slug_category) #displays all events with unique slug_category
    paginator = Paginator(events, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    # data to be displayed in filter section menu
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')

    context = {
        "category" : category,
        "name" : category_name,
        "event_categories" : event_categories,
        "events" : paged_events,
        'genres' : genres,
        "covers" : cover_image,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "categories/category.html", context)