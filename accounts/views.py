from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomerLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def customer_signup_view(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful. You can now log in.")
            return redirect('login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'signup.html', {'form': form})


def customer_login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('profile')
    else:
        form = CustomerLoginForm()
    return render(request, 'login.html', {'form': form})


def customer_logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
