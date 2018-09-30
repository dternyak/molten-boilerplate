from invoke import task


@task
def test(c, cov=False, verbose=False):
    c.run("export ENVIRONMENT=test")
    pytest_command = 'pytest tests'
    if cov:
        pytest_command += ' --cov=api'
    if verbose:
        pytest_command += ' -s '
    c.run(pytest_command)


@task
def start(c, log_level='info'):
    c.run("export ENVIRONMENT=common")
    gunicorn_command = 'gunicorn --reload app:app'
    gunicorn_command += ' --log-level={}'.format(log_level)
    print(gunicorn_command)
    c.run(gunicorn_command)
