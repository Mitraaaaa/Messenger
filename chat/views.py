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
    chat = Chat.objects.filter(name=room_name).first()
    msgs = []

    if chat:
        msgs = Message.objects.filter(chat=chat)
    else:
        chat = Chat(name=room_name, type='Group')
        chat.save()

    return render(request, 'room.html', {
        'room_name': room_name,
        'msgs': msgs
    })

# remmeber to creat a buttton for uploading the file
# def UploadFile(request):
#     if request.method == "POST" :
#         form = upload_file(request.POST, request.FILES)
#     else :
#        form= upload_file()
#     return render(request,'file_transfer.html',{"form" : form})
