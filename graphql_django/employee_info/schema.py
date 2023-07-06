import graphene
from employee_info.models import Person as db_Person
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
        return db_Person.objects.all().select_related('address')


schema = graphene.Schema(query=Query)