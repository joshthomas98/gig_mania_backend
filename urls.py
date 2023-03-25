from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list),
    path('bands/<int:id>', views.band_detail),
    path('venues/', views.venue_list),
    path('venues/<int:id>', views.venue_detail),
    path('bands/validate/<str:email>/<str:password>/', views.validate_band_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)
