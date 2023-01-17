from django.shortcuts import render, redirect
from .models import Message, Chat
import json
# from .forms import upload_file


def home(request):
    return render(request, 'home.html')


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    # friends = json.loads("friends.json")
    # friends_list = friends[request.user]
    return render(request, "roomName.html", context)


def room(request, room_name):
    x = room_name.split("_")
    chat = Chat.objects.filter(type=x[0]).filter(name=x[1]).first()
    msgs = []

    if chat:
        msgs = Message.objects.filter(chat=chat)
    else:
        chat = Chat(name=x[1], type=x[0])
        chat.save()

    return render(request, 'room.html', {
        'room_name': x[1],
        'msgs': msgs
    })

# remmeber to creat a buttton for uploading the file
# def UploadFile(request):
#     if request.method == "POST" :
#         form = upload_file(request.POST, request.FILES)
#     else :
#        form= upload_file()
#     return render(request,'file_transfer.html',{"form" : form})
