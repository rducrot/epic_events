from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Client, Contract, Event
from app.serializers import ClientListSerializer, ClientDetailSerializer, ContractListSerializer, \
                            ContractDetailSerializer, EventListSerializer, EventDetailSerializer
from app.permissions import ClientPermission, ContractPermission, EventPermission
from authentication.models import User


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
    """
    ViewSet for Client object.
    Authentication is required.
    Support Users can only see clients from events assigned to them.
    Sales Users can only see clients assigned to them and potential clients.
    """
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name', 'email']

    def get_queryset(self):
        if self.request.user.team == User.Team.SUPPORT:
            return Client.objects.filter(contract__event__support_contact=self.request.user).distinct()
        elif self.request.user.team == User.Team.SALES:
            return Client.objects.filter(
                Q(sales_contact=self.request.user) | Q(client_status=Client.ClientStatus.POTENTIAL))
        return Client.objects.all()
    

class ContractViewSet(ModelViewSet, MultipleSerializerMixin):
    """
    ViewSet for Contract object.
    Authentication is required.
    Support Users can only see contracts related to their assigned events.
    Sales Users can only see contracts assigned to them.
    """
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated, ContractPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'date_created', 'amount']

    def get_queryset(self):
        if self.request.user.team == User.Team.SUPPORT:
            return Contract.objects.filter(event__support_contact=self.request.user)
        elif self.request.user.team == User.Team.SALES:
            return Contract.objects.filter(sales_contact=self.request.user)
        return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)
        

class EventViewSet(ModelViewSet, MultipleSerializerMixin):
    """
    ViewSet for Event object.
    Authentication is required.
    Support Users can only see events assigned to them.
    Sales Users can only see events related to their assigned contracts.
    """
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated, EventPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contract__client__last_name', 'contract__client__email', 'event_date']

    def get_queryset(self):
        if self.request.user.team == User.Team.SUPPORT:
            return Event.objects.filter(support_contact=self.request.user)
        elif self.request.user.team == User.Team.SALES:
            return Event.objects.filter(contract__sales_contact=self.request.user)
        return Event.objects.all()
