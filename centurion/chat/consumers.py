import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from channels.db import database_sync_to_async
from django.utils import timezone 
from django.utils.formats import date_format
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        room_name = self.room_name
        created_at = timezone.now()
        formatted_created_at = date_format(created_at, "H:i")


        # Save message to database
        await self.save_message(username, room_name, message, created_at)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "username": username, "created_at": formatted_created_at}
        )

    async def save_message(self, username, room, message_text, created_at):
        user = await database_sync_to_async(User.objects.get)(username=username)
        message = Message(
            message=message_text,
            username=user,
            created_at=created_at,  # Make sure to import timezone from django.utils
            room=room
        )
        await database_sync_to_async(message.save)()

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        created_at = event["created_at"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "username": username, "created_at": created_at}))