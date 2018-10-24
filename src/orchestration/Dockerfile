FROM python

WORKDIR /orchservice

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "apiserve.py"]