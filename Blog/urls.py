from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from Index.views import index
from PublicationAdd.views import add_publication

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', index),
    re_path(r'^add/', add_publication),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)