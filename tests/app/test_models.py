from datetime import datetime

import pytz

import pytest

from app import models
from authentication.models import User


@pytest.mark.django_db
class TestClass:

    def setup_method(self):
        self.sales_contact = User.objects.create_user(username='Toto', team=User.Team.SALES)
        self.support_contact = User.objects.create_user(username='Titi', team=User.Team.SUPPORT)
        self.client = models.Client.objects.create(
            first_name='Toto',
            last_name='Toto',
            email='toto@mail.com',
            phone='0102030405',
            mobile='0607080910',
            company_name='Toto Company',
            sales_contact=self.sales_contact,
        )
        self.contract = models.Contract.objects.create(
            contract_status=models.Contract.ContractStatus.SIGNED,
            amount=50,
            payment_due=datetime(2023, 5, 15, 14, 0, 0, tzinfo=pytz.UTC),
            client=self.client,
            sales_contact=self.sales_contact,
        )

    def test_create_client(self, client_fixture):
        sut = models.Client.objects.create(
            first_name=client_fixture['first_name'],
            last_name=client_fixture['last_name'],
            client_status=client_fixture['client_status'],
            email=client_fixture['email'],
            phone=client_fixture['phone'],
            mobile=client_fixture['mobile'],
            company_name=client_fixture['company_name'],
            sales_contact=self.sales_contact,
        )
        assert isinstance(sut, models.Client)

    def test_create_client_wrong_sales_contact(self, client_fixture):
        sut = models.Client.objects.create(
            first_name=client_fixture['first_name'],
            last_name=client_fixture['last_name'],
            client_status=client_fixture['client_status'],
            email=client_fixture['email'],
            phone=client_fixture['phone'],
            mobile=client_fixture['mobile'],
            company_name=client_fixture['company_name'],
            # Register wrong user for sales_contact
            sales_contact=self.support_contact,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()

    def test_create_contract(self, contract_fixture):
        sut = models.Contract.objects.create(
            contract_status=contract_fixture['contract_status'],
            amount=contract_fixture['amount'],
            payment_due=contract_fixture['payment_due'],
            client=self.client,
            sales_contact=self.sales_contact,
        )
        assert isinstance(sut, models.Contract)

    def test_create_contract_wrong_sales_contact(self, contract_fixture):
        sut = models.Contract.objects.create(
            contract_status=contract_fixture['contract_status'],
            amount=contract_fixture['amount'],
            payment_due=contract_fixture['payment_due'],
            client=self.client,
            # Register wrong user for sales_contact
            sales_contact=self.support_contact,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()

    def test_create_event(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            event_status=event_fixture['event_status'],
            attendee=event_fixture['attendee'],
            event_date=event_fixture['event_date'],
            notes=event_fixture['notes'],
            contract=self.contract,
            support_contact=self.support_contact,
        )
        assert isinstance(sut, models.Event)

    def test_create_event_wrong_support_contact(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            event_status=event_fixture['event_status'],
            attendee=event_fixture['attendee'],
            event_date=event_fixture['event_date'],
            notes=event_fixture['notes'],
            contract=self.contract,
            # Register wrong user for support_contact
            support_contact=self.sales_contact,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()
            