FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

RUN useradd -m appuser

EXPOSE 5000

USER appuser
CMD ["python", "app.py"]
