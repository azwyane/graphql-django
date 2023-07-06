from django.test import TestCase
from graphene.test import Client
from employee_info.schema import schema


class PeopleTestCase(TestCase):
    """
    Test case for the people GraphQL query.

    Attributes:
        client (Client): The GraphQL client.
        query (str): The GraphQL query to be executed.
        response (dict): The response received from the GraphQL server.
        data (dict): The data extracted from the response.

    """
    def setUp(self):
        """
        Set up the test case.

        This method initializes the GraphQL client, defines the GraphQL query,
        executes the query, and extracts the response data.

        """
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

