from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    if password == request.POST['confirm-password']:
      try:
        user = User.objects.get(username=username)
        return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
      except User.DoesNotExist:
        user = User.objects.create_user(username, password)
        auth.login(request, user)
        return redirect('home')
    else:
      return render(request, 'accounts/signup.html', {'error': 'Passwords Must Math'})
  else:
    return render(request, 'accounts/signup.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect.'})

  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('home')

@login_required(login_url="/accounts/login")
def view_profile(request, user_id):
  args = {
    'user': User.objects.get(pk=user_id)
  }

  return render(request, 'accounts/profile.html', args)

@login_required(login_url="/accounts/login")
def edit_profile(request, user_id):
  args = {
    'user': User.objects.get(pk=user_id)
  }

  return render(request, 'accounts/edit_profile.html', args)
