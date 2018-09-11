# eboutique/views.py

from rest_framework import viewsets
from erp.models import *
from eboutique.serializers import *

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
