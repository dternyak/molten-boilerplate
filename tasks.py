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
def start(c):
    c.run("export ENVIRONMENT=common")
    c.run('gunicorn --reload app:app')
