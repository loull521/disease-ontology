import os
import sys 
import site

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'disease_ontology.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
