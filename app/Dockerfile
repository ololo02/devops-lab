FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y curl wget

EXPOSE 5000

CMD ["python", "app.py"]
