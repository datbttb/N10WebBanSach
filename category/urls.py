from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from category import views

urlpatterns = [
    path('create/',views.getform, name='create'),
    path('themsanpham',views.themsanpham),
    path('sanpham', views.dssanpham),
    path('edit/<id>', views.editform),
    path('suasp',views.suasanpham)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
