from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomLoginForm, RegisterForm
from accounts.models import UserProfile, User


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            password = form.cleaned_data['password']
            profile.save()
            profile.user.set_password(password)
            profile.user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_view')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username/email or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required(login_url='login_view')
def profile(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    return render(request, 'auth/userprofile.html', {'userprofile': userprofile})


def update_profile(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    context = {
        'userprofile': userprofile,
        'user': user,
    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        username = request.POST.get('username')

        UserProfile.objects.filter(user=user).update(first_name=first_name,
                                                     last_name=last_name,
                                                     address=address,
                                                     username=username)
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_view')




    return render(request, 'auth/update.html', context )