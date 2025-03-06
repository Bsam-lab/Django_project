from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("shop/", views.shop, name='shop'),
    path("shop_detail/", views.shop_detail, name="shop_detail"),
    path("cart/", views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("error/", views.error, name='error'),
    path("contact/", views.contact, name='contact')
]