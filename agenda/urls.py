from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', include('contact.urls')),
    path('todo/', include('todo.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
