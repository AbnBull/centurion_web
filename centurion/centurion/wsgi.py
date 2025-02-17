import os
from django.core.wsgi import get_wsgi_application

# Specify module if it isnt already
os.environ['DJANGO_SETTINGS_MODULE'] = 'centurion.settings.production'

# expose application
application = get_wsgi_application()
