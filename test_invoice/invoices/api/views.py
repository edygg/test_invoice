from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers as invoices_serializers
from .. import models as invoices_models


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = invoices_models.Invoice.objects.all()
    serializer_class = invoices_serializers.InvoiceSerializer


class TestApiView(APIView):

    def get(self, request, format=None):
        return Response(dict(hola="mundo"))
