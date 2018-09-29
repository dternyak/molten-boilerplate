# Molten-Boilerplate

## Usage

1. Install requirements `pip install -r requirements.txt`
2. run the app with `gunicorn app:app`.

## Example requests

    $ curl -F'name=mittens' http://127.1:8000/v1/kittens
    $ curl http://127.1:8000/v1/kittens
    $ curl http://127.1:8000/v1/kittens/1
