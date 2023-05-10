from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('artists/', views.artist_list),
    path('artists/<int:id>/', views.artist_detail),

    path('availabilities/', views.availability_list),
    path('availabilities/<int:id>/', views.availability_detail),

    path('venues/', views.venue_list),
    path('venues/<int:id>/', views.venue_detail),

    path('artists/validate/', views.artist_sign_in),
    path('venues/validate/', views.venue_sign_in),

    path('artist_listed_gigs/', views.artist_listed_gig_list),
    path('artist_listed_gigs/<int:id>/', views.artist_listed_gig_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
