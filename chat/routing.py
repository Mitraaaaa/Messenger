from django.urls import path, re_path
from chat.consumers import ChatConsumer
from . import consumers

websocket_urlpatterns = [
    #path("" , ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
