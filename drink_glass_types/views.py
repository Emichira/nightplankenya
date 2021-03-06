from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import GlassType
from drink_categories.models import DrinkCategory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from genres.models import Genre
from categories.models import Category

def category(request, slug_category):
    #handles display of cocktails belonging to a single category
    category = DrinkCategory.objects.filter(slug=slug_category) #slugify url
    if category.exists():
        category = category.first()
    else:
        raise Http404
    category_name = DrinkCategory.objects.get(slug=slug_category)
    #display all cover images in detailed category
    cover_image = Event.objects.exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    #displays all cocktails with unique slug_category
    cocktails = Event.objects.order_by('event_date').filter(categories__slug=slug_category)
    paginator = Paginator(cocktails, 16)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)
    # data to be displayed in filter section menu
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')

    context = {
        "event_categories" : event_categories,
        "name" : category_name,
        "event_categories" : event_categories,
        "cocktails" : paged_cocktails,
        'genres' : genres,
        "covers" : cover_image,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "categories/cocktail-categories.html", context)