FROM python:alpine3.17
COPY requirements.txt .
RUN pip install disnake
COPY app/ /app
WORKDIR /app
CMD ["python3", "followBot.py"]