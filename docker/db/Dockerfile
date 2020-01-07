FROM yuxiqian/felis-catus-base
EXPOSE 5432
ADD src_tmp/ /
ENTRYPOINT ["./bind_db.sh", "deadloop.sh"]
