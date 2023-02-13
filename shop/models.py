from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from company.models import Company

class ProductName(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey('Supplier', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    product = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class StockIn(models.Model):
    quantity = models.IntegerField(default=0)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    price_in = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice = models.IntegerField(default=0)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
 
   
    def __str__(self):
        return self.name


class Invoice(models.Model):
    
    PAYMENT_MPESA = 'MPesa'
    PAYMENT_CASH = 'Cash'
    PAYMENT_BANK = 'Bank'

    PAYMENT_CHOICES = [
        (PAYMENT_MPESA, 'MPesa'),
        (PAYMENT_CASH, 'Cash'),
        (PAYMENT_BANK, 'Bank'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES, default=0)
    payment_details = models.TextField(default="please Provide details")
    created_by = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True, default=1)
    invoice_number = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f" {self.invoice_number} - ${self.created_by}"


class Sales(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
   

    
