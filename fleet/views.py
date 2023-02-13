from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import NewVehicleRegistrationSerializer , InvoicesSerializer , ProformaSerializer, DocumentsRegistrationSerializer, UploadingOfDocumentsPerVehicleSerializer, ExpensePerVehicleSerializer
from .models import NewVehicleRegistration, Invoices, Proforma, DocumentsRegistration, UploadingOfDocumentsPerVehicle, ExpensePerVehicle




class NewVehicleRegistartionViewSet(ModelViewSet):
    queryset = NewVehicleRegistration.objects.all()
    serializer_class = NewVehicleRegistrationSerializer
    permission_classes = [IsAuthenticated]    


class InvoicesViewSet(ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    permission_classes = [IsAuthenticated] 


class ProformaViewSet(ModelViewSet):
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer
    permission_classes = [IsAuthenticated] 


class DocumentsRegistrationViewSet(ModelViewSet):
    queryset = DocumentsRegistration.objects.all()
    serializer_class = DocumentsRegistrationSerializer
    permission_classes = [IsAuthenticated] 


class UploadingOfDocumentsPerVehicleViewSet(ModelViewSet):
    queryset = UploadingOfDocumentsPerVehicle.objects.all()
    serializer_class = UploadingOfDocumentsPerVehicleSerializer
    permission_classes = [IsAuthenticated] 


class ExpensePerVehicleViewSet(ModelViewSet):
    queryset = ExpensePerVehicle.objects.all()
    serializer_class = ExpensePerVehicleSerializer
    permission_classes = [IsAuthenticated] 


