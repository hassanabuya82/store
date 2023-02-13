from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from company.models import Company

class NewVehicleRegistration(models.Model):
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    vehicle_price = models.DecimalField(max_digits=8, decimal_places=2)
    plate_no = models.CharField(max_length=255)
    chassis_no = models.CharField(max_length=255)
    
    def __str__(self):
        return self.plate_no

class DocumentsRegistration(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class UploadingOfDocumentsPerVehicle(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    document = models.ForeignKey(DocumentsRegistration, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.document.name}"


class Invoices(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.invoice_no}"

class Proforma(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    proforma_no = models.CharField(max_length=255)
    proforma_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.proforma_no}"



class ExpensePerVehicle(models.Model):
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255)
    expense_date = models.DateTimeField(auto_now_add=True)
    expense_amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.vehicle} - {self.expense_name}"