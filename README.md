# graphql-django

```
# Django GraphQL Service

This project is a Django-based GraphQL service that exposes a GraphQL endpoint for retrieving a list of people with pagination. The service is designed using a schema-first approach and follows best practices for Django web development.

## Features

- GraphQL endpoint at `/graphql`
- Schema-first approach
- Pagination support for the `people` query
- `Person` and `Address` models with corresponding database tables
- Sample data for `Person` and `Address` models
- Dockerized development environment using Docker Compose
- Unit test for the GraphQL endpoint

## Installation and Setup

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for running the service in a containerized environment)

### Getting Started without docker

1. Clone the repository:

   ```bash
   git clone https://github.com/azwyane/graphql-django.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Load sample data:

   ```bash
   python manage.py loaddata sample_data.json
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The GraphQL endpoint will be available at `http://localhost:8000/graphql`.

### Dockerized Development Environment

 Make sure you have Docker installed. 

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the Docker container:

   ```bash
   docker-compose up
   ```

   The GraphQL endpoint will be available at `http://localhost:8000/graphql`.

### Running Tests

To run the unit test for the GraphQL endpoint, use the following command:

```bash
python manage.py test
```
