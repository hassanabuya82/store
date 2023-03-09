from myauth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductNameSerializer, ProductDetailsSerializer, StockInSerializer, CustomerSerializer, UserSerializer, SupplierSerializer, InvoiceSerializer, SalesSerializer
from .models import ProductName, ProductDetails, StockIn, Customer, Supplier, Invoice, Sales



class ProductNameViewSet(ModelViewSet):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailsViewSet(ModelViewSet):
    serializer_class = ProductDetailsSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        product_name_id = self.kwargs.get('product_name_id')
        return ProductDetails.objects.filter(product_id=product_name_id)


class StockInViewSet(ModelViewSet):
    queryset = StockIn.objects.all()
    serializer_class = StockInSerializer
    permission_classes = [IsAuthenticated]    


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]    


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]    


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]    


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]


class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]



