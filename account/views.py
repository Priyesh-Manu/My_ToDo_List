
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        # Get user input from the form
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        create_password = request.POST['crpassword']
        conform_password = request.POST['cnpassword']
        
        # Check if passwords match
        if create_password == conform_password:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                # Create a new user and save to the database
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=create_password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords didn\'t match')
            return redirect('signup')
    return render(request, 'signup.html')

# Function for user login
def user_login(request):
    if request.method == 'POST':
        # Get user input from the login form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in and redirect to home
            login(request, user)
            name= username.capitalize()
            messages.info(request,''+name)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

# Function for user logout
def user_logout(request):
    # Logout the user and redirect to home
    logout(request)
    return redirect('home')
