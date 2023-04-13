from django.conf import settings
from django.db import models

from authentication.models import User


class TimeStampModel(models.Model):
    """
    Base model for time stamp.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(TimeStampModel):
    """
    Client model.
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)

    class ClientStatus(models.TextChoices):
        POTENTIAL = "Potential"
        EXISTING = "Existing"
    
    client_status = models.CharField(max_length=16, choices=ClientStatus.choices, default=ClientStatus.POTENTIAL)

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        limit_choices_to={'team':User.Team.SALES})

    def __str__(self):
        return f'{self.first_name} { self.last_name} - {self.company_name}'


class Contract(TimeStampModel):
    """
    Contract model.
    """

    class ContractStatus(models.TextChoices):
        NEW = "New"
        SIGNED = "Signed"

    contract_status = models.CharField(max_length=16, choices=ContractStatus.choices, default=ContractStatus.NEW)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        limit_choices_to={'team':User.Team.SALES})


    def __str__(self):
        return f'{self.client} - Contract {self.pk}'


class Event(TimeStampModel):
    """
    Event model.
    """

    class EventStatus(models.TextChoices):
        NEW = "New"
        CURRENT = "Current"
        FINISHED = "Finished"

    event_status = models.CharField(max_length=16, choices=EventStatus.choices, default=EventStatus.NEW)
    attendee = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()

    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, limit_choices_to={'contract_status':Contract.ContractStatus.SIGNED})
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        limit_choices_to={'team':User.Team.SUPPORT})

    def __str__(self):
        return f'{self.client} - Event {self.pk}'
