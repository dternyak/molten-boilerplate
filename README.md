# Molten-Boilerplate

## What's included?
- SQLAlchemy
- alembic
- camelCase API
- py.test (with coverage)

## Usage
Install requirements

```
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

Adjust `settings.toml` with your `DATABASE_URL` on `common` and `test`.

For now, `common` represents both production and dev.

Finally, run:

```
alembic upgrade head
```

If you make changes to your model,
you'll need to adjust `migrations/env` to import any new models.

Then, run:

```
alembic revision -m "New thing did" --autogenerate
```



### Dev
`export ENVIRONMENT="common" &&  gunicorn --reload app:app`

### Test
`export ENVIRONMENT="test" && pytest tests`    
