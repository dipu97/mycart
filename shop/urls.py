
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/about/', views.about, name='aboutUs'),
    path('shop/contact/', views.contact, name='contactUs'),
    path('shop/tracking/', views.tracking, name='track'),
    path('shop/search', views.search, name='search'),
    path('shop/product/', views.product, name='product'),
]
