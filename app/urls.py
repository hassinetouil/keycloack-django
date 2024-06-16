from django.urls import path
from .views import ProductListView  # or product_list_view

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    # or for function-based view
    # path('products/', product_list_view, name='products'),
]
