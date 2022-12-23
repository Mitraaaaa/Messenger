from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import os
from django.core.asgi import get_asgi_application
from chat import routing as rt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Server.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                rt.websocket_urlpatterns
            )
        )
    }
)
