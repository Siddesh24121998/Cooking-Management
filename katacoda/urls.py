

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from . import settings

from . import healthz

urlpatterns = [
    url(r'^healthz/ready', healthz.ready),
    url(r'^healthz/alive', healthz.alive),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
