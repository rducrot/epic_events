from rest_framework import serializers

from app import models
from authentication.serializers import UserSerializer


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = ['first_name', 'last_name', 'email', 'company_name']


class ClientDetailSerializer(serializers.ModelSerializer):

    sales_contact = serializers.SerializerMethodField()

    class Meta:
        model = models.Client
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'sales_contact']
    
    def get_sales_contact(self, instance):
        queryset = instance.sales_contact
        serializer = UserSerializer(queryset, read_only=True)
        return serializer.data


class ContractListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = ['id', 'contract_status', 'amount', 'payment_due']

class ContractDetailSerializer(serializers.ModelSerializer):

    sales_contact = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    class Meta:
        model = models.Contract
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'sales_contact']

    def get_sales_contact(self, instance):
        queryset = instance.sales_contact
        serializer = UserSerializer(queryset, read_only=True)
        return serializer.data
    
    def get_client(self, instance):
        queryset = instance.client
        serializer = ClientListSerializer(queryset, read_only=True)
        return serializer.data


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = ['id', 'event_status', 'attendee', 'event_date', 'notes']


class EventDetailSerializer(serializers.ModelSerializer):

    support_contact = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'support_contact']
    
    def get_support_contact(self, instance):
        queryset = instance.support_contact
        serializer = UserSerializer(queryset, read_only=True)
        return serializer.data