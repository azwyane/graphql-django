import graphene
from employee_info.models import Person as db_Person
from django.core.paginator import Paginator

class Person(graphene.ObjectType):
    email = graphene.String(required=True)
    name = graphene.String(required=True)
    address = graphene.Field('employee_info.schema.Address')

class Address(graphene.ObjectType):
    number = graphene.Int(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    state = graphene.Field('employee_info.schema.StateEnum')

class StateEnum(graphene.Enum):
    STATE_A = 'State A'
    STATE_B = 'State B'
    STATE_C = 'State C'

class Query(graphene.ObjectType):
    people = graphene.List(Person, page=graphene.Int(), limit=graphene.Int())

    def resolve_people(self, info, page=None, limit=None):
        # Set default values for page and limit if not provided
        page = page or 1
        limit = limit or 10

        persons = db_Person.objects.order_by('id').all().select_related('address')
        
        # Create a Paginator object with the desired limit
        paginator = Paginator(persons, limit)

        # Validate the requested page number
        total_pages = paginator.num_pages
        if page < 1 or page > total_pages:
            raise ValueError("Invalid page number")

        requested_page = paginator.page(page)
        return requested_page


schema = graphene.Schema(query=Query)