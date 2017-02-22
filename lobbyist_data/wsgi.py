import os, sys

from django.core.wsgi import get_wsgi_application


sys.path.append("c:/cygwin64/home/kaebnickk/lobbyist_data")
os.environ["DJANGO_SETTINGS_MODULE"] = "lobbyist_data.settings"
application = get_wsgi_application()
