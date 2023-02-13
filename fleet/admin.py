from django.contrib import admin
from . models import NewVehicleRegistration, DocumentsRegistration, UploadingOfDocumentsPerVehicle, Invoices, Proforma, ExpensePerVehicle
# Register your models here.

@admin.register(NewVehicleRegistration)
class NewVehicleRegistrationAdmin(admin.ModelAdmin):
    list_display = ['registered_by', 'registered_on', 'plate_no', 'chassis_no'] 

@admin.register(DocumentsRegistration)
class DocumentsRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','registered_on'] 

@admin.register(UploadingOfDocumentsPerVehicle)
class UploadingOfDocumentsPerVehicleAdmin(admin.ModelAdmin):
    list_display = ['name','vehicle', 'document','uploaded_on'] 

@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'invoice_no','created_on'] 

@admin.register(Proforma)
class ProformaAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'proforma_no','created_on'] 

@admin.register(ExpensePerVehicle)
class ExpensePerVehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'expense_name', 'expense_date', 'expense_amount'] 

