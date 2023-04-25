from rest_framework import serializers

from app import models
from authentication.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):

    sales_contact = serializers.SerializerMethodField()

    class Meta:
        model = models.Client
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'sales_contact']
    
    def get_sales_contact(self, instance):
        queryset = instance.sales_contact
        serializer = UserSerializer(queryset)
        return serializer.data


class ContractSerializer(serializers.ModelSerializer):

    sales_contact = serializers.SerializerMethodField()

    class Meta:
        model = models.Contract
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'sales_contact']

    def get_sales_contact(self, instance):
        queryset = instance.sales_contact
        serializer = UserSerializer(queryset)
        return serializer.data


class EventSerializer(serializers.ModelSerializer):

    support_contact = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated', 'support_contact']
    
    def get_support_contact(self, instance):
        queryset = instance.support_contact
        serializer = UserSerializer(queryset)
        return serializer.data
