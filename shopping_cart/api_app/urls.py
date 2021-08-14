from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCart.as_view()),
]