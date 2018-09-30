from invoke import task


@task
def test(c, cov=False, verbose=False):
    pytest_command = 'export ENVIRONMENT=test && pytest tests'
    if cov:
        pytest_command += ' --cov=api'
    if verbose:
        pytest_command += ' -s '
    c.run(pytest_command)


@task
def start(c, log_level='info'):
    gunicorn_command = 'export ENVIRONMENT=common && gunicorn --reload app:app'
    gunicorn_command += ' --log-level={}'.format(log_level)
    c.run(gunicorn_command)
