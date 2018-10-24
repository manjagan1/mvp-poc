FROM python

WORKDIR /orchservice

# Pip install
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY data ./data/
COPY . .

CMD ["python", "apiserve.py"]