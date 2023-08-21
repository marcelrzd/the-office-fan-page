"""
URL configuration for to_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # Fetch and save data from office api
    path('fetch-and-save-seasons/', FetchAndSaveSeasons.as_view(),
         name='fetch-and-save-seasons'),
    path('fetch-and-save-characters/', FetchAndSaveCharacters.as_view(),
         name='fetch-and-save-characters'),
    path('fetch-and-save-episodes/', FetchAndSaveEpisodes.as_view(),
         name='fetch-and-save-episodes'),

    # Fetch data from database
    path('fetch-seasons/', FetchSeasons.as_view(), name='fetch-seasons'),
    path('fetch-episodes/', FetchEpisodes.as_view(), name='fetch-episodes'),
    path('fetch-characters/', FetchCharacters.as_view(), name='fetch-characters'),
    path('fetch-random-quote/', FetchRandomQuote.as_view(),
         name='fetch-random-quote'),
]
