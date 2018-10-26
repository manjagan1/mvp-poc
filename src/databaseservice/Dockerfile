FROM microsoft/mssql-tools

WORKDIR /dbservice

RUN apt-get update && apt-get install -y python3 python-pip gcc g++ build-essential u:nixodbc-dev

COPY ./requirements.txt ./requirements.txt

#RUN pip install -r requirements.txt

COPY . .

CMD ["python", "mssqlservice.py"]