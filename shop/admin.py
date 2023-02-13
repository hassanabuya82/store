from django.contrib import admin
from .models import ProductName,ProductDetails, StockIn, Invoice, Customer, Sales, Supplier

# Register your models here.

@admin.register(ProductName)
class ProductNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier'] 

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity','description','price','created_at'] 

@admin.register(StockIn)
class StockInAdmin(admin.ModelAdmin):
    list_display = ['quantity','product', 'supplier', 'price_in', 'selling_price','invoice'] 

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['payment_method','payment_details','invoice_number', 'created_by','created_on', 'total_amount'] 

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone', 'email'] 

@admin.register(Sales)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['invoice',  'product', 'discount', 'quantity'] 

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name',  'location', 'phone'] 

