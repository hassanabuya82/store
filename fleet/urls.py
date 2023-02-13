from django.urls import path
from . import views

urlpatterns = [
    path('fleet/', views.NewVehicleRegistartionViewSet.as_view({'get': 'list', 'post': 'create'}), name="fleet"),
    path('fleet/<int:pk>/', views.NewVehicleRegistartionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('invoices/', views.InvoicesViewSet.as_view({'get': 'list', 'post': 'create'}), name="invoices"),
    path('invoices/<int:pk>/', views.InvoicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('proforma/', views.ProformaViewSet.as_view({'get': 'list', 'post': 'create'}), name="proforma"),
    path('proforma/<int:pk>/', views.ProformaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('DocumentsRegistration/', views.DocumentsRegistrationViewSet.as_view({'get': 'list', 'post': 'create'}), name="DocumentsRegistration"),
    path('DocumentsRegistration/<int:pk>/', views.DocumentsRegistrationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('UploadingOfDocuments/', views.UploadingOfDocumentsPerVehicleViewSet.as_view({'get': 'list', 'post': 'create'}), name="UploadingOfDocumentsPerVehicle"),
    path('UploadingOfDocuments/<int:pk>/', views.UploadingOfDocumentsPerVehicleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('Expense/', views.ExpensePerVehicleViewSet.as_view({'get': 'list', 'post': 'create'}), name="ExpensePerVehicle"),
    path('Expense/<int:pk>/', views.ExpensePerVehicleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    ]