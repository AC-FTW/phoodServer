from django.conf.urls import url
from django.contrib import admin

from .views import form, label, labelMetamind

urlpatterns = [
    url(r'^form/$', form, name='form'),
    url(r'^label/$', label, name='label'),
    url(r'^labelMetamind/$', labelMetamind, name='labelMetamind'),
]