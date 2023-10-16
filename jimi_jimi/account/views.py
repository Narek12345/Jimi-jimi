from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from .forms import UserRegistrationForm


def dashboard(request):
	return render(request, 'dashboard.html')


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
			messages.success(request, 'Registration completed successfully')
			return redirect('account:dashboard')
	else:
		form = UserRegistrationForm()
	return render(request, 'account/register.html', {'form': form})


def logout(request):
	messages.success(request, 'You have successfully logged out')
	auth_logout(request)
	return render(request, 'dashboard.html')