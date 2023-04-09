import pytest

from app import models
from authentication.models import User


@pytest.mark.django_db
class TestClass:

    def setup_method(self):
        self.sales_contact = User.objects.create_user(username='Toto', team='Sales')
        self.support_contact = User.objects.create_user(username='Titi', team='Support')
        self.client = models.Client.objects.create(
            first_name='Toto',
            last_name='Toto',
            email='toto@mail.com',
            phone='0102030405',
            mobile='0607080910',
            company_name='Toto Company',
            sales_contact=self.sales_contact,
        )

    def test_create_client(self, client_fixture):
        sut = models.Client.objects.create(
            first_name=client_fixture['first_name'],
            last_name=client_fixture['last_name'],
            email=client_fixture['email'],
            phone=client_fixture['phone'],
            mobile=client_fixture['mobile'],
            company_name=client_fixture['company_name'],
            sales_contact=self.sales_contact,
        )
        assert isinstance(sut, models.Client)

    def test_create_contract(self, contract_fixture):
        assert not models.Contract.objects.exists()

        sut = models.Contract.objects.create(
            status=contract_fixture['status'],
            amount=contract_fixture['amount'],
            payment_due=contract_fixture['payment_due'],
            client=self.client,
            sales_contact=self.sales_contact,
        )
        assert isinstance(sut, models.Contract)

    def test_create_event(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            attendee=event_fixture['attendee'],
            event_date=event_fixture['event_date'],
            notes=event_fixture['notes'],
            client=self.client,
            support_contact=self.support_contact,
        )
        assert isinstance(sut, models.Event)
