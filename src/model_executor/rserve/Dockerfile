FROM r-base:3.5.1

WORKDIR /rbase-server

RUN install.r Rserve && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Set Workdir for R as RHOME
ENV RSERVE_HOME /rbase-server

RUN useradd rserve && usermod -d . rserve

# Copy over config files
COPY etc etc

RUN chown -R rserve:rserve .

USER rserve

# Set username and password
#ENV USERNAME ${USERNAME:-rserve}
#ENV PASSWORD ${PASSWORD:-rserve}


RUN mkdir ./workdir

EXPOSE 6311

CMD ["R", "-e", "library(Rserve)", "-e", "run.Rserve(config.file ='./etc/Rserve.conf')"]