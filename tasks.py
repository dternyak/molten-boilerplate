from invoke import task


@task
def test(c, cov=False, verbose=False):
    pytest_command = 'export ENVIRONMENT=test && pytest tests'
    if cov:
        pytest_command += ' --cov=api'
    if verbose:
        pytest_command += ' -s '
    c.run(pytest_command, pty=True)


@task
def start(c, log_level='info', port=5000):
    gunicorn_command = 'export ENVIRONMENT=common && export PORT={} && gunicorn --reload app:app'.format(port)
    gunicorn_command += ' --log-level={}'.format(log_level)
    c.run(gunicorn_command, pty=True)


@task
def shell(c):
    command = 'export ENVIRONMENT="common" && ./scripts/interpreter'
    c.run(command, pty=True)
