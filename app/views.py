from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from app.models import Client, Contract, Event
from app.serializers import ClientListSerializer, ClientDetailSerializer, ContractListSerializer, \
                            ContractDetailSerializer, EventListSerializer, EventDetailSerializer
from app.permissions import ClientPermission, ContractPermission, EventPermission


class MultipleSerializerMixin:
    """
    Mixin that returns a serializer depending on list or detail view.
    """
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewSet(ModelViewSet, MultipleSerializerMixin):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated, ClientPermission]

    def get_queryset(self):
        return Client.objects.all()
    

class ContractViewSet(ModelViewSet, MultipleSerializerMixin):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated, ContractPermission]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(ModelViewSet, MultipleSerializerMixin):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated, EventPermission]

    def get_queryset(self):
        return Event.objects.all()
