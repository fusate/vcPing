FROM python:alpine3.17
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ /app
WORKDIR /app
CMD ["python3", "followBot.py"]