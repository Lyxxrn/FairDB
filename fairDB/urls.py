from django.urls import path
from .views import ProductView, UserReviewListCreateView, UserReviewDetailView, ProductDetailView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductView.as_view(), name='product-update'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('reviews/', UserReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', UserReviewDetailView.as_view(), name='review-detail'),
]