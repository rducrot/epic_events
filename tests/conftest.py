from datetime import datetime
import pytz

import pytest
from django.test import Client


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def client_fixture():
    data = {
        'first_name': 'Toto',
        'last_name': 'DUPONT',
        'email': 'toto@mail.com',
        'phone': '04.10.10.20.20',
        'mobile': '06.01.02.03.04',
        'company_name': 'Toto Company',
    }
    return data


@pytest.fixture
def contract_fixture():
    data = {
        'status': True,
        'amount': 1200.25,
        'payment_due': datetime(2023, 6, 15, 0, 0, 0, tzinfo=pytz.UTC),
    }
    return data


@pytest.fixture
def event_fixture():
    data = {
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
        'team': 'Manager',
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
        'team': 'Sales',
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
        'team': 'Support',
    }
    return data
