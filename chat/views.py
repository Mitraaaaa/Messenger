from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "roomName.html", context)


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
