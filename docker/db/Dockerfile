FROM python:3
EXPOSE 5432
ADD src_tmp/ /
RUN pip install -r requirements.txt
RUN ./utils/install_pg.sh
RUN ./init_db.sh < '\n'
RUN ./init_link.sh < '\n'
RUN python ./gen_rb.py
RUN ./init_data.sh
