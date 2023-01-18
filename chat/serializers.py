from rest_framework import serializers
from .models import Chat, Message

# Serializer for Chat Model
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["name"]

# Serializer for Message Model
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["chat", "sender", "type", "time", "text", "seen"]