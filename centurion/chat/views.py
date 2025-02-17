from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.
@login_required
def room(request, room_name):

    # Fetch messages for the given room
    messages = Message.objects.filter(room=room_name).order_by("created_at")

    # get ws scheme
    if request.is_secure():
        ws_scheme = "wss"
    else:
        ws_scheme = "ws"

    # Pass the messages to the template context
    context = {
        "room_name": room_name,
        "messages": messages,
        "ws_scheme": ws_scheme,
    }
    return render(request, "chat/room.html", context)
