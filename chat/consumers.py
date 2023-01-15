import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Chat
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.roomGroupName = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username

        # Find Room Object
        room = await database_sync_to_async(Chat.objects.get)(name=self.room_name)

        # Create New Message Object
        Msg = Message(
            text = message,
            chat = room,
            sender = self.scope['user'],
            type = 'tx'
        )

        await database_sync_to_async(Msg.save)()

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        # await self.save_msg(self.scope['user'], self.room_name, message, 'tx')
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username
        }))

    


    async def Recieve_file(self, Tfile):
        file = json.loads(Tfile)
        f = file(

        )

        
   

    @database_sync_to_async
    def save_msg(sender, chat, text, type):
        return Message.objects.create(sender=sender, chat=chat, text=text, type=type)
