FROM python:3
EXPOSE 5432
ADD ../src/ /
ADD ../requirements.txt /
RUN pip install -r requirements.txt
RUN ./init_db.sh < '\n'
RUN ./init_link.sh < '\n'
RUN python ./gen_rb.py
RUN ./init_data.sh
