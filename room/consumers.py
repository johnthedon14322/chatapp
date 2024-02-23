import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from room.models import Messages

from django.core.mail import send_mail


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "room"
        self.room_group_name = f"chat"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        user = text_data_json.get("user")

        print(message)

        Messages.objects.create(message=message, user=user)

        email_message = f'from {user}, - {message}'


        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "user" : user}
        )



    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "user" : user}))