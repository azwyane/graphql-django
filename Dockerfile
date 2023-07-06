# Use an official Python(v 3.9) runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container workdir
COPY graphql_django/ .

# Expose port 8000 of container
EXPOSE 8000

# Run the command to migrate database
CMD ["python","manage.py", "migrate"]

# Run the command to load fixtures
CMD ["python","manage.py", "loaddata", "sample"]

# Run the command to start Django Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

