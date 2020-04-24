from django.urls import path
from .views import *



urlpatterns = [
    #path('', IndexView.as_view()),
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view()),
    path('contact.html/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('cart.html/', ContactView.as_view(), name='cart'),

]
