from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('new_page', views.new_page, name='new_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
