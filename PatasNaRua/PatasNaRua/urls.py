from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadlog/', include('cadlog.urls')),
    path('', include('app_initial.urls')),  # Adicione esta linha para incluir as URLs do app_initial
]

