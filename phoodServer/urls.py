from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', TemplateView.as_view(template_name="home.html")),
    url(r'^nutrition/', include("nutritionLabel.urls")),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

