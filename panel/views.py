from django.utils import timezone
from django.db import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Invoice, Sales, ProductName
from fleet.models import Invoices

class DashboardView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        # Get today's date
        today = timezone.localdate()

        # Total products sold today
        total_products_sold = Sales.objects.filter(invoice__created_on__date=today).count()

        # Amount sold today
        amount_sold = Sales.objects.filter(invoice__created_on__date=today).aggregate(
            total_amount=models.Sum('invoice__total_amount')
        )['total_amount']

        # Number of invoices generated today
        invoices_generated = Invoice.objects.filter(created_on__date=today).count() + Invoices.objects.filter(created_on__date=today).count()

        # Products in today
        products_in_today = ProductName.objects.filter(sales__invoice__created_on__date=today).count()

        # Return the results
        return Response({
            'total_products_sold': total_products_sold,
            'amount_sold': amount_sold,
            'invoices_generated': invoices_generated,
            'products_in_today': products_in_today,
        })
