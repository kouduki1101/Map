from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('Icon.urls')),
                  path('', include('maplist.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
