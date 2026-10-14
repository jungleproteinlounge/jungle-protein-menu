from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu.views import menu_home
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", menu_home, name="menu_home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
