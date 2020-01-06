FROM python:3
EXPOSE 5432
ADD src_tmp/ /
RUN ./install_pg.sh
RUN pip install -r requirements.txt
RUN ./init_db_as_postgres.sh
RUN ./init_link.sh
RUN python ./gen_rb.py
RUN ./init_data.sh
