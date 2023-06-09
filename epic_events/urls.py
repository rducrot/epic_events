"""epic_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from app.views import ClientViewSet, ContractViewSet, EventViewSet


API_PATH = 'api/'

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'contracts', ContractViewSet, basename='contract')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PATH, include(router.urls)),
    path(API_PATH + 'login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(API_PATH + 'login/token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
