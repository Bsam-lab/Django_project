from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path("", views.index, name='index'),
    path("shop/", views.shop, name='shop'),
    path("shop_detail/", views.shop_detail, name="shop_detail"),
    path("cart/", views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("error/", views.error, name='error'),
    path("contact/", views.contact, name='contact'),
    path("register/", views.register, name='register'),
    path('login/', views.login, name='login')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)