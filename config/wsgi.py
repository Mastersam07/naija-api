import os

from django.core.wsgi import get_wsgi_application
import dotenv

dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_wsgi_application()
