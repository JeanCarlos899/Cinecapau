from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
from . import views   

app_name = 'cineflix'

urlpatterns = [ 
    path('', views.MovieList.as_view(), name='movie_list'),
    path('detail/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('update/<int:pk>', views.MovieUpdate.as_view(), name='movie_update'),
    path('delete/<int:pk>', views.MovieDelete.as_view(), name='movie_delete'),
    path('create', movie_criate, name = 'movie_create'), 

]  
  
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)