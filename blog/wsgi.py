import os

import sys

sys.path.append('/home/centos/blog')

os.environ.setdefault("PYTHON_EGG_CACHE", "/home/centos/blog/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
