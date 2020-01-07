FROM yuxiqian/felis-docker-base
EXPOSE 5432
ADD src_tmp/ /
RUN ./init_db_as_postgres.sh
RUN ./init_link.sh
RUN python ./gen_rb.py
RUN ./init_data.sh
