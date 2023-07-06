from django.db import models
from enum import Enum
from django.core.paginator import Paginator
class StateEnum(Enum):
    """
    Enumeration of possible states.

    Possible values:
        STATE_A: State A
        STATE_B: State B
        STATE_C: State C
    """
    STATE_A = 'State A'
    STATE_B = 'State B'
    STATE_C = 'State C'

class Address(models.Model):
    """
    Represents an address.

    Attributes:
        number (int): The street number.
        street (str): The name of the street.
        city (str): The city.
        state (str): The state of the address, chosen from the StateEnum.
    """
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=50, choices=[(state.name, state.value) for state in StateEnum])

    def __str__(self):
        return f"{self.number} {self.street} {self.city} {self.state}"

class Person(models.Model):
    """
    Represents a person.

    Attributes:
        email (str): The email of the person.
        name (str): The name of the person.
        address (Address): The address of the person.
    """
    email = models.EmailField()
    name = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} : {self.email}"

    @classmethod
    def get_page(cls,page:int,limit:int):
        persons = cls.objects.order_by('id').all().select_related('address')
        
        # Create a Paginator object with the desired limit
        paginator = Paginator(persons, limit)

        # Validate the requested page number
        total_pages = paginator.num_pages
        if page < 1 or page > total_pages:
            raise ValueError("Invalid page number")

        requested_page = paginator.page(page)
        return requested_page
