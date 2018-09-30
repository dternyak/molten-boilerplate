import logging
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
DEBUG = ENVIRONMENT == "dev"
LOGGER = logging.getLogger(__name__)

port = os.getenv("PORT") or "8000"
bind = f"0.0.0.0:{port}"
reload = DEBUG

timeout = 30
graceful_timeout = 15

workers = 4 if not DEBUG else 1
worker_class = "gthread"

errorlog = "-"
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
