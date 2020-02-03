from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about-us/', views.about_page, name='about'),
    path('terms&conditions/', views.terms_and_conditions_page, name='terms'),
    path('faq/', views.faq_page, name='faq'),
    path('team/', views.team_page, name='team')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)