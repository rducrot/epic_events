from datetime import datetime

import pytest
import pytz

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
            #amount=contract_fixture['amount'],
            payment_due=datetime(2023, 5, 15, 14, 0, 0, tzinfo=pytz.UTC),
            client=self.client,
            sales_contact=self.sales_contact,
        )
        self.contract_unsigned = models.Contract.objects.create(
            contract_status=models.Contract.ContractStatus.NEW,
            amount=50,
            payment_due=datetime(2023, 5, 15, 14, 0, 0, tzinfo=pytz.UTC),
            client=self.client,
            sales_contact=self.sales_contact,
        )

    def test_create_client(self, client_fixture):
        sut = models.Client.objects.create(
            sales_contact=self.sales_contact,
            **client_fixture,
            )
        assert isinstance(sut, models.Client)

    def test_create_client_wrong_sales_contact(self, client_fixture):
        sut = models.Client.objects.create(
            # Register wrong user for sales_contact
            sales_contact=self.support_contact,
            **client_fixture,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()

    def test_create_contract(self, contract_fixture):
        sut = models.Contract.objects.create(
            client=self.client,
            sales_contact=self.sales_contact,
            **contract_fixture,
        )
        assert isinstance(sut, models.Contract)

    def test_create_contract_wrong_sales_contact(self, contract_fixture):
        sut = models.Contract.objects.create(
            client=self.client,
            # Register wrong user for sales_contact
            sales_contact=self.support_contact,
            **contract_fixture,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()

    def test_create_event(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            contract=self.contract,
            support_contact=self.support_contact,
            **event_fixture,
        )
        assert isinstance(sut, models.Event)

    def test_create_event_wrong_support_contact(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            contract=self.contract,
            # Register wrong user for support_contact
            support_contact=self.sales_contact,
            **event_fixture,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()

    def test_create_event_wrong_contract(self, event_fixture):
        assert not models.Event.objects.exists()

        sut = models.Event.objects.create(
            contract=self.contract_unsigned,
            support_contact=self.support_contact,
            **event_fixture,
        )
        with pytest.raises(TypeError):
            sut.full_clean()
            sut.save()
