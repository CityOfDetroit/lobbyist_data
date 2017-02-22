from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from lookup import views

urlpatterns = [
    url(r'^$', views.lookup),
    url(r'^lookup/', include('lookup.urls', namespace="lookup")),
]
