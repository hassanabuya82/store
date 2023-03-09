from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', views.ProductNameViewSet.as_view({'get': 'list', 'post': 'create'}), name="product-list"),
    path('products/<int:pk>/', views.ProductNameViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('products/<int:product_name_id>/details/', views.ProductDetailsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:product_name_id>/details/<int:pk>/', views.ProductDetailsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('stock', views.StockInViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('stock/<int:pk>', views.StockInViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  
    path('customers', views.CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('customers/<int:pk>', views.CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})), 
    path('users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('suppliers', views.SupplierViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('suppliers/<int:pk>', views.SupplierViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('invoice', views.InvoiceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('invoice/<int:pk>', views.InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('sales', views.SalesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('sales/<int:pk>', views.SalesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
]