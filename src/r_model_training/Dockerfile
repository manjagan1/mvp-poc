FROM python

WORKDIR /r_model_training

# Pip install
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y r-base

# Copy project files
COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]