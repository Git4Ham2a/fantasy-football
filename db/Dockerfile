FROM mysql:5.7 
ENV MYSQL_DATABASE=flask-db
COPY ./create.sql docker-entrypoint-initdb.d/create.sql
