from django.contrib import admin
from django.urls import path
from gestionpedidos import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.renderview, name='home'),
    path('register/', app_views.register, name='register'),
    path('houses/', app_views.houses_list, name='houses'),
    path('contact/', app_views.contact, name='contact'),
    path('login/', app_views.login, name='loginnn'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

