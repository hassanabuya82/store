from .models import ProductName, ProductDetails, StockIn, Customer, Supplier, Invoice, Sales
from rest_framework import serializers
from myauth.models import User


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = ['name', 'supplier']

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['product', 'description', 'price', 'quantity', 'created_at']

class StockInSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockIn
        fields = ['quantity','supplier','product', 'price_in', 'selling_price', 'invoice']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'address', 'phone', 'email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'location', 'phone']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['payment_method', 'payment_details', 'created_by', 'invoice_number', 'created_on', 'total_amount']

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['quantity', 'product', 'discount', 'invoice']


