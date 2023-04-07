import pytest

from django.conf import settings

from app import models
from authentication.models import User



class TestClass:

    @pytest.mark.django_db
    def setup_class(self, sales_fixture, support_fixture, client_fixture):
        sales_user = User.objects.create(username='Toto')


    @pytest.mark.django_db
    def test_client_model(self, client_fixture):
        assert not models.Client.objects.exists()

        sut = models.Client.objects.create(
            first_name=client_fixture['first_name'],
            last_name=client_fixture['last_name'],
            email=client_fixture['email'],
            phone=client_fixture['phone'],
            mobile=client_fixture['mobile'],
            company_name=client_fixture['company_name'],
        )
        assert isinstance(sut, models.Client)

    @pytest.mark.django_db
    def test_contract_model(self, contract_fixture):
        assert not models.Contract.objects.exists()

        sut = models.Contract.objects.create(
            status=contract_fixture['status'],
            amount=contract_fixture['amount'],
            payment_due=contract_fixture['payment_due'],
        )
        assert isinstance(sut, models.Contract)


    @pytest.mark.django_db
    def test_event_model(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            attendee=event_fixture['attendee'],
            event_date=event_fixture['event_date'],
            notes=event_fixture['notes'],
        )
