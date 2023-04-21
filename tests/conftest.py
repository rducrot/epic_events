from datetime import datetime

from django.test import Client
import pytest
import pytz

from app import models
from authentication.models import User

@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def client_fixture():
    data = {
        'first_name': 'Toto',
        'last_name': 'DUPONT',
        'client_status': models.Client.ClientStatus.EXISTING,
        'email': 'toto@mail.com',
        'phone': '04.10.10.20.20',
        'mobile': '06.01.02.03.04',
        'company_name': 'Toto Company',
    }
    return data


@pytest.fixture
def contract_fixture():
    data = {
        'contract_status': models.Contract.ContractStatus.SIGNED,
        'amount': 1200.25,
        'payment_due': datetime(2023, 6, 15, 0, 0, 0, tzinfo=pytz.UTC),
    }
    return data

@pytest.fixture
def contract_unsigned_fixture(contract_fixture):
    contract_fixture['contract_status'] = models.Contract.ContractStatus.NEW
    return contract_fixture


@pytest.fixture
def event_fixture():
    data = {
        'event_status': models.Event.EventStatus.NEW,
        'attendee': 50,
        'event_date': datetime(2023, 5, 15, 14, 0, 0, tzinfo=pytz.UTC),
        'notes': 'An event for Toto Company',
    }
    return data


@pytest.fixture
def manager_fixture():
    data = {
        'username': 'manager_user',
        'first_name': 'Jane',
        'last_name': 'DOE',
        'email': 'manager@mail.com',
        'password': 'Jane@1234!',
        'team': User.Team.SALES,
    }
    return data


@pytest.fixture
def sales_fixture():
    data = {
        'username': 'sales_user',
        'first_name': 'John',
        'last_name': 'DOE',
        'email': 'sales@mail.com',
        'password': 'mdp*Sales44!',
        'team': User.Team.SALES,
    }
    return data


@pytest.fixture
def support_fixture():
    data = {
        'username': 'support_user',
        'first_name': 'Jean',
        'last_name': 'DUPONT',
        'email': 'support@mail.com',
        'password': 'Dup0nt123mdp!',
        'team': User.Team.SUPPORT,
    }
    return data
