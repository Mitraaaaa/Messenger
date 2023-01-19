from django.shortcuts import render, redirect
from .models import Message, Chat
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "roomName.html", context)


def room(request, room_name):
    x = room_name.split("_")
    if x[0] == 'Group' or x[1] == 'Channel':
        chat = Chat.objects.filter(name=room_name).first()
    else:
        if Chat.objects.filter(name=room_name).exists():
            print(room_name, "found")
            chat = Chat.objects.filter(name=room_name).first()
        else:
            print(room_name, " not found")
            chat = Chat.objects.filter(name=f'{x[1]}_{x[0]}').first()
    msgs = []

    if chat:
        msgs = Message.objects.filter(chat=chat)
    else:
        print('creating new chatRoom', room_name)
        chat = Chat(name=room_name)
        chat.save()

    return render(request, 'room.html', {
        'room_name': room_name,
        'msgs': msgs
    })


def account(request, username):
    return render(request, 'account.html', {})


def deleteAcc(request, username):
    u = User.objects.filter(username=username)
    if u.exists():
        u.delete()
        return render(request, 'home.html', {})
    else:
        print("Unknown Error!")


def editFirstName(request, username, new_fname):
    u = User.objects.get(username=username)
    u.first_name = new_fname
    u.save()
    return render(request, 'roomName.html', {})



def editLastName(request, username, new_lname):
    u = User.objects.get(username=username)
    u.last_name = new_lname
    u.save()
    return render(request, 'roomName.html', {})



def editUsername(request, username, new_username):
    if User.objects.filter(username=new_username).exists():
        print("Username has been used!")
    else:
        u = User.objects.filter(username=username).first()
        u.username = new_username
        u.save()

    return render(request, 'roomName.html', {})


def editEmail(request, username, new_email):
    if User.objects.filter(email=new_email).exists():
        print("Email has been used!")
    else:
        u = User.objects.filter(username=username).first()
        u.email = new_email
        u.save()

    return render(request, 'roomName.html', {})
