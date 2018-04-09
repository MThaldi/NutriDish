from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.nutri_homes, name='nutri_homes'),
    url(r'^menu$',views.menu,name='menu'),
    url(r'^contactus$',views.n_contactus, name='contactus'),
]