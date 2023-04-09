from django.conf import settings
from django.db import models


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

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} { self.last_name} - {self.company_name}'


class Contract(TimeStampModel):
    """
    Contract model.
    """
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.client} - Contract {self.pk}'


class Event(TimeStampModel):
    """
    Event model.
    """

    class Status(models.TextChoices):
        NEW = "New"
        CURRENT = "Current"
        FINISHED = "Finished"

    event_status = models.CharField(max_length=16, choices=Status.choices)
    attendee = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.client} - Event {self.pk}'
