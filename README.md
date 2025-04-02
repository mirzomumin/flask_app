# Mini Flask App

The Flask app with Redis - caching service and containerization with Docker

## Set Up

1. Clone the project repository

```shell
git clone git@github.com:mirzomumin/flask_app.git
```

2. Move to the project directory

```shell
cd flask_app
```

3. Create `.env` file and copy the content of `.env-example` file into it with default parameters.

```shell
cp .env-example .env
```
You can change `.env` file parameters value at any time as you wish.

## Launch project

1. Launch the app with Docker

```shell
docker compose up --build -d
```

## API Endpoints

1. GET /ping → Check flask app liveness

Request
```shell
curl -X 'GET' \
  'http://127.0.0.1:5000/ping' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json'
```

Response
```shell
{"status":"ok"}
```

2. GET /count → Return visit count

Request
```shell
curl -X 'GET' \
  'http://127.0.0.1:5000/count' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json'
```

Response
```shell
{"visit_count": 12}
```

## Stop project
1. Stop and remove containers, networks

```shell
docker compose down
```
