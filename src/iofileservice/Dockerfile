FROM python

WORKDIR /ioservice

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "io_file_service.py"]