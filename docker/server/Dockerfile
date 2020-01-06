FROM python:3
EXPOSE 8080
ADD ../src/ /
ADD ../requirements.txt /
RUN pip install -r requirements.txt
RUN ./run_server.sh