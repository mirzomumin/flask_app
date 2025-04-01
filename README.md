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

## Launch

1. Launch the project with Docker

```shell
docker compose up --build -d
```
