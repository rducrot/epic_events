from rest_framework import permissions

from authentication.models import User


class ClientPermission(permissions.BasePermission):
    """
    Management and Support Users can GET list and retrieve.
    Sales Users have all rights.
    """

    def has_permission(self, request, view):
        if request.user.team in (User.Team.SUPPORT, User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.team == User.Team.SALES


class ContractPermission(permissions.BasePermission):
    """
    Management and Support Users can GET list and retrieve.
    Sales Users have all rights.
    """

    def has_permission(self, request, view):
        if request.user.team in (User.Team.SUPPORT, User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.team == User.Team.SALES


class EventPermission(permissions.BasePermission):
    """
    Management Users can GET list and retrieve.
    Support Users can GET list and retrieve, UPDATE assigned events.
    Sales Users have all rights.
    """

    def has_permission(self, request, view):
        if request.user.team == User.Team.MANAGEMENT:
            return request.method in permissions.SAFE_METHODS
        elif request.user.team == User.Team.SUPPORT:
            return request.method in ['GET', 'PUT', 'PATCH']
        else:
            return request.user.team == User.Team.SALES

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.team in (User.Team.SALES, User.Team.SUPPORT)
        elif view.action == 'destroy':
            return request.user.team == User.Team.SALES
