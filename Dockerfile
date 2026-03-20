FROM python:3.13-slim

WORKDIR /crypto_etl

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]