from django.conf.urls import url
from django.conf.urls.static import static
from shorturls.views import *
from django.conf import settings


urlpatterns = [
    url('^(.+)$', redir),
    url('^$', home),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)