from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'', include('home.urls')),
    url(r'home&', include('home.urls')),
    url(r'^menu&',include('home.urls')),
    url(r'^contactus&', include('home.urls')),
]
