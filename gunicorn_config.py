import os
import sys
import multiprocessing

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Gunicorn configuration
bind = "0.0.0.0:" + str(int(os.environ.get("PORT", 5000)))
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2
timeout = 120
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info" 
