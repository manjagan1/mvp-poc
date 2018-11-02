FROM r-base:3.5.1

WORKDIR /rbase-server

RUN install.r Rserve && \
    rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# you have to run Rserve with remote=TRUE otherwise
# it won't let you connect to the container
EXPOSE 6311
CMD ["R", "-e", "Rserve::run.Rserve(remote=TRUE)"]


