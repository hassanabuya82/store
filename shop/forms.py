from django.forms import ModelForm
from .models import Sales,  ProductName, ProductDetails, StockIn, Supplier, Customer, Invoice

class SalesForm(ModelForm):
    class Meta:
        model = Sales 
        fields = '__all__'

class ProductNameForm(ModelForm):
    class Meta:
        model = ProductName 
        fields = '__all__'

class ProductDetailsForm(ModelForm):
    class Meta:
        model = ProductDetails 
        fields = '__all__'

class StockInForm(ModelForm):
    class Meta:
        model = StockIn 
        fields = '__all__'

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier 
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = '__all__'

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice 
        fields = '__all__'
