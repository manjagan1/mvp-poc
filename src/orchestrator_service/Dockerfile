FROM python

WORKDIR /orchestrator_service

# Pip install
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
#RUN apt-get update && apt-get install -y r-base

# Copy project files
COPY . .

CMD ["python", "manage.py"]