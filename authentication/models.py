from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices


class User(AbstractUser):
    """
    Base model for user.
    Permissions depend on the team selection.
    """
    
    class Team(TextChoices):
        MANAGEMENT = 'Management'
        SALES = 'Sales'
        SUPPORT = 'Support'
    
    team = CharField(choices=Team.choices, blank=False, null=False, max_length=16)

