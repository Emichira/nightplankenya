from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.files.images import ImageFile
from .models import Event
from cocktails.models import Cocktail
from categories.models import Category
from counties.models import County
from clubs.models import Club
from drink_categories.models import DrinkCategory
from genres.models import Genre
from django.http import HttpResponse, Http404
from django.db.models import Q
from datetime import datetime, date
from itertools import chain

def events(request):
    #create objects
    #Handles displaying of all events
    events = Event.objects.filter(is_published=True).order_by('event_date')
    cover_image = Event.objects.filter(is_published=True).order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    #pagination of events
    paginator = Paginator(events, 20)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    # data to be displayed in filter section menu
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')

    context = {
        "events" : paged_events,
        "event_categories" : event_categories,
        "covers" : cover_image,
        'genres' : genres,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "events/events.html", context)

def event(request, slug_event):
    #create one object event to detailed view event
    #Handles displaying of single event
    tonight = Event.objects.filter(event_date__date=date.today())
    event = get_object_or_404(Event, slug=slug_event)
    classics = Cocktail.objects.filter(categories='1').order_by('-updated_at')

    context = {
        "event" : event,
        "tonight" : tonight,
        'classics' : classics,
    }
    return render(request, "events/event.html", context)

def search(request):
    #search based function for events, venue and counties
    queryset_event = Event.objects.order_by('event_date')
    queryset_cocktail = Cocktail.objects.order_by('updated_at')
    query = request.GET.get('q')
    # if query not None:
    if query != "":
        queryset_cocktail = queryset_cocktail.filter(Q(name__icontains=query) |
            Q(alcohol__name__icontains=query) | Q(categories__name__icontains=query) |
                Q(club__name__icontains=query) | Q(glass_type__name__icontains=query) |
                    Q(cocktail_recipe_author__icontains=query)).distinct()
    else:
        pass
        # queryset_event = queryset_event.filter(Q(title__icontains=query) |
        #     Q(county__name__icontains=query) | Q(categories__name__icontains=query)).distinct()
        # q3 = list(chain(queryset_cocktails, queryset_event))

    cover_image = Event.objects.filter(is_published=True).order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    #pagination of rendered cocktails
    paginator = Paginator(queryset_cocktail, 20)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "cocktails" : paged_cocktails,
        "event_categories" : event_categories,
        "covers" : cover_image,
        'genres' : genres,
        'query' : query,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "events/search.html", context)