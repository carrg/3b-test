FROM python:3.12.4-alpine3.20

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt 

EXPOSE 5000

CMD ["python3", "app.py"]