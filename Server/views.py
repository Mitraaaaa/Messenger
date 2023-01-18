from django.shortcuts import render
from user.models import custom_user
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email , RegexValidator
from chat.views import room
from django.shortcuts import redirect

def sign_up(request):
    return render(request , 'signup.html')

def validateUser(request):
    if request.method == 'POST':
        name = request.POST['room-name-input']
        if not User.objects.filter(username = name):
            notice = "this user doesn't exist"
            action = 'enter a valid username'
            return render(request , 'roomName.html' , {'notice' : notice , 'action' : action})
        else:
            if request.POST['select1'] == "Group" or request.POST['select1'] == "Channel":
                response = redirect('/chat/' + request.POST['select1'] + "_" + name)
                return response
            else:
                response = redirect('/chat/' + request.user.username + "_" + name)
                return response
                

            # response = redirect('/chat/' + request.POST[] + "_" + name)
            # return response
            # return render(request, )

