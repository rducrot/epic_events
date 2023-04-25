from rest_framework import permissions

from app.models import Client
from authentication.models import User


class ClientPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.team in (User.Team.SUPPORT, User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES

    def has_object_permission(self, request, view, obj):
        if request.user.team == User.Team.SUPPORT:
            return obj in Client.objects.filter(contract__event__support_contract=request.user)


class ContractPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.team in (User.Team.SUPPORT, User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES
            
    def has_object_permission(self, request, view, obj):
        pass


class EventPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.team == User.Team.MANAGEMENT:
            return request.method in permissions.SAFE_METHODS
        elif request.user.team == User.Team.SUPPORT:
            return request.method in ['GET', 'PUT']
        else:
            return request.user.team == User.Team.SALES
            

    def has_object_permission(self, request, view, obj):
        pass
