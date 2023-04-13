

from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls.static import static

from . import settings

from . import healthz

urlpatterns = [
    re_path(r'^healthz/ready', healthz.ready),
    re_path(r'^healthz/alive', healthz.alive),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
