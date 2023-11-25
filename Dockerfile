FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app


RUN pip install sqlalchemy psycopg2-binary
#RUN pip install beautifulsoup4
RUN pip install requests


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
