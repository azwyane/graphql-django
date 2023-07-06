from django.test import TestCase
from graphene.test import Client
from employee_info.schema import schema


class PeopleTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.query = '''
            query {
                people(page: 1, limit: 10) {
                    email
                    name
                    address {
                        number
                        street
                        city
                        state
                    }
                }
            }
        '''

        self.response = self.client.execute(self.query)
        self.data = self.response['data']


    def test_people_is_a_list(self):
        self.assertIsInstance(self.data['people'], list)
    
    def test_address_is_available(self):
        peoples = self.data['people']
        for person in peoples:
            self.assertIn('address', person)

