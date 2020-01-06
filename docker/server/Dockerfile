FROM python:3
EXPOSE 8080
ADD src_tmp/ /
RUN pip install -r requirements.txt
CMD [ "./run_server.sh" ]