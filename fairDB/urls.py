from django.conf.urls.static import static
from django.urls import path

from FairProduct import settings
from .api_views import *
from .views import *

urlpatterns = [

    # API routes
    path('products/', ProductView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductView.as_view(), name='product-update'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('reviews/', UserReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', UserReviewDetailView.as_view(), name='review-detail'),
    path('rate-product/', rate_product, name='rate_product'),

    # frontend routes
    path('', index, name='index'),
    path('api/search/', ProductSearchView.as_view(), name='search_products'),
    path('product/<str:barcode>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)