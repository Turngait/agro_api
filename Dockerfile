FROM python:3.7

RUN pip install mysqlclient
RUN pip install Flask flask-sqlalchemy Flask-PyMongo
RUN pip install -U flask-cors
WORKDIR /app
COPY app /app

EXPOSE 9090 9191

CMD ["python", "main.py"]