from .models import NewVehicleRegistration, DocumentsRegistration, UploadingOfDocumentsPerVehicle, Invoices, Proforma, ExpensePerVehicle
from rest_framework import serializers


class NewVehicleRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewVehicleRegistration
        fields = '__all__'

        
class DocumentsRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsRegistration
        fields = '__all__'

        
class UploadingOfDocumentsPerVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadingOfDocumentsPerVehicle
        fields = '__all__'

        
class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'

        
class ProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proforma
        fields = '__all__'

        
class ExpensePerVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensePerVehicle
        fields = '__all__'

        