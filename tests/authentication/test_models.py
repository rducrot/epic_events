import pytest

from authentication import models


@pytest.mark.django_db
class TestClass:

    def test_create_manager_user(self, manager_fixture):
        sut = models.User.objects.create_user(
            username=manager_fixture['username'],
            first_name=manager_fixture['first_name'],
            last_name=manager_fixture['last_name'],
            email=manager_fixture['email'],
            password=manager_fixture['password'],
            team=manager_fixture['team'],
        )
        assert isinstance(sut, models.User)
        assert sut.team == 'Manager'

    def test_create_sales_user(self, sales_fixture):
        sut = models.User.objects.create_user(
            username=sales_fixture['username'],
            first_name=sales_fixture['first_name'],
            last_name=sales_fixture['last_name'],
            email=sales_fixture['email'],
            password=sales_fixture['password'],
            team=sales_fixture['team'],
        )
        assert isinstance(sut, models.User)
        assert sut.team == 'Sales'

    def test_create_support_user(self, support_fixture):
        sut = models.User.objects.create_user(
            username=support_fixture['username'],
            first_name=support_fixture['first_name'],
            last_name=support_fixture['last_name'],
            email=support_fixture['email'],
            password=support_fixture['password'],
            team=support_fixture['team'],
        )
        assert isinstance(sut, models.User)
        assert sut.team == 'Support'
