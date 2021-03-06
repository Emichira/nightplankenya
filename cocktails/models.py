from django.db import models
from datetime import datetime
from drink_categories.models import DrinkCategory
from drink_glass_types.models import GlassType
from alcohol.models import Alcohol
from clubs.models import Club
from django.urls import reverse
from django.utils.translation import activate

class Cocktail(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    cocktail_image = models.ImageField(upload_to='images/cocktail/%Y/%m/%d/')
    video_tutorial = models.URLField(max_length=200, null=True, blank=True)
    categories = models.ManyToManyField(DrinkCategory, blank=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, null=True, blank=True)
    glass_type = models.ForeignKey(GlassType, on_delete=models.CASCADE, null=True, blank=True)
    block_quote = models.CharField(max_length=66, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    cocktail_recipe_author = models.CharField(max_length=200, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })