from rest_framework import serializers
from .. import models as invoices_models


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = invoices_models.Invoice
        fields = ["client_name", "client_address", "refers_to"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
    	    "client_name": instance.client_name,
            "client_address": instance.client_address,
            "refers_to": instance.refers_to,
        }