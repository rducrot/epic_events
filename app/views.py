from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from app.models import Client, Contract, Event
from app.serializers import ClientSerializer, ContractSerializer, EventSerializer
from app.permissions import ClientPermission, ContractPermission, EventPermission


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]

    def get_queryset(self):
        return Client.objects.all()
    

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermission]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]

    def get_queryset(self):
        return Event.objects.all()
