from rest_framework.viewsets import ModelViewSet

from app import models, serializers


class ClientViewSet(ModelViewSet):
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects.all()
    

class ContractViewSet(ModelViewSet):
    serializer_class = serializers.ContractSerializer

    def get_queryset(self):
        return models.Contract.objects.all()


class EventViewSet(ModelViewSet):
    serializer_class = serializers.EventSerializer

    def get_queryset(self):
        return models.Event.objects.all()
