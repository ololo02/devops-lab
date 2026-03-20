FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN useradd -m appuser

EXPOSE 5000

USER appuser
CMD ["python", "app.py"]
