# Molten-Boilerplate

## Usage
Install requirements `pip install -r requirements.txt`

Adjust `settings.toml` with your `DATABASE_URL`.

`alembic upgrade head`

### Dev
`export ENVIRONMENT="common" &&  gunicorn --reload app:app`

### Test
`export ENVIRONMENT="test" && pytest tests`    
