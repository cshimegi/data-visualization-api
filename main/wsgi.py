"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

# add the project path into the sys.path
sys.path.append('/vagrant')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/env38/lib/python3.8/site-packages')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "main.settings"

application = get_wsgi_application()
