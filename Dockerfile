FROM python:3.9

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK CMD [ "curl", "http://127.0.0.1:5000/ping" ]

EXPOSE 5000

CMD ["gunicorn", "app:app"]
