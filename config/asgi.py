import os

from django.core.asgi import get_asgi_application
import dotenv

dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_asgi_application()
