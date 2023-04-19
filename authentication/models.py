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

    REQUIRED_FIELDS = ['password', 'team']

    def save(self, *args, **kwargs):
        if self.team == self.Team.MANAGEMENT:
            self.is_staff = True
            self.is_superuser = True
        else :
            self.is_staff = False
            self.is_superuser = False
        
        user = super(User, self)
        user.save()
        return user
