from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bands/', views.band_list),
    path('bands/<int:id>/', views.band_detail),

    path('availabilities/', views.availability_list),
    path('availabilities/<int:id>/', views.availability_detail),

    path('venues/', views.venue_list),
    path('venues/<int:id>/', views.venue_detail),

    path('bands/validate/', views.band_sign_in),

    path('artist_listed_gigs/', views.artist_listed_gig_list),
    path('artist_listed_gigs/<int:id>/', views.artist_listed_gig_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
