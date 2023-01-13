from django.shortcuts import render
from user.models import custom_user
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email , RegexValidator

def sign_up(request):
    return render(request , 'signup.html')

def create_user(request):

    if request.method == 'POST':
    
        #getting user info
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        #password validation
        try:
            validate_password(password)
        except:
            notice = 'not a valid password'
            action = 'please use atleast 8 character'
            return render(request , 'signup.html' , {'notice' : notice , 'action' : action})

        #email validation
        try:
            validate_email(email)
        except:
            notice = 'not a valid email'
            return render(request , 'signup.html' , {'notice' : notice})

        #check if a user with this email has already signed in
        #if custom_user.user.objects.filter(user = email):
        if User.objects.filter(username = email):
            notice = 'a user with this email address has already signed in'
            action = 'try a new email or log in'
            return render(request , 'signup.html' , {'notice' : notice , 'action' : action})

        #create new user and save the info
        u = User()
        u.username = email
        u.first_name = first_name
        u.last_name = last_name
        u.set_password(password)
        u.save()

        newUser = custom_user()
        newUser.user = u
        newUser.phone_number = phone_number
        newUser.save()

        return render(request , 'home.html')
    
    else:
        return render(request , 'signup.html')
    
    
    #if custom_user.user.objects.filter(user = user):
       #notice = 'this phone number has been used'
       #action = 'please use a new phone number'
       #return render(request , 'signup.html' , {"notice" : notice, 'action' : action})
    #else:
        #create_user = custom_user(user = user , phone_number = phone_number)
        #notice = 'new user was successfully created'
        #action = 'please log in'
        #return render(request , 'home.html' , {'notice' : notice , 'action' : action})

