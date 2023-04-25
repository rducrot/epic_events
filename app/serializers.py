from rest_framework import serializers

from app import models


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']
