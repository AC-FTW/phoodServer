from django.conf.urls import url
from django.contrib import admin

from .views import form, label

urlpatterns = [
    url(r'^form/$', form, name='form'),
	url(r'^label/$', label, name='label'),
]
