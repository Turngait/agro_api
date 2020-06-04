FROM python:3.7

RUN pip install mysqlclient
RUN pip install Flask flask-sqlalchemy Flask-PyMongo Flask-MongoAlchemy
RUN pip install -U flask-cors
RUN pip install pycrypto
WORKDIR /app
COPY app /app

EXPOSE 9090 9191

CMD ["python", "main.py"]