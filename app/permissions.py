from rest_framework import permissions

from authentication.models import User


class ClientPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.team == (User.Team.SUPPORT or User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES

    def has_object_permission(self, request, view, obj):
        pass


class ContractPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.team == (User.Team.SUPPORT or User.Team.MANAGEMENT):
            return request.method in permissions.SAFE_METHODS
        else:
            return request.user.team == User.Team.SALES
            
    def has_object_permission(self, request, view, obj):
        pass


class EventPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        pass
