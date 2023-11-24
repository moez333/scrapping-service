FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

# Install additional dependencies for database
RUN pip install sqlalchemy psycopg2-binary
RUN pip install beautifulsoup4
RUN pip install requests


# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
