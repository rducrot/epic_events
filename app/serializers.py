from rest_framework import serializers

from app import models


class ClientStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client.ClientStatus
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = '__all__'
        read_only_fields = ['id']
    
    def get_client_status(self, instance):
        queryset = instance.client_status
        serializer = ClientStatusSerializer(queryset)
        return serializer.data


class ContractStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract.ContractStatus
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = '__all__'
        read_only_fields = ['id']


class EventStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event.EventStatus
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id']
