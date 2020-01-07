FROM postgres:11
EXPOSE 5432
ENV POSTGRES_PASSWORD '123456'
ENV POSTGRES_USER 'felis'
ENV POSTGRES_DB 'felis'

ADD ./db/initi.sql /docker-entrypoint-initdb.d/schema.sql