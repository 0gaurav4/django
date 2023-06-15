from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful. Please login.')
            return redirect('success')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup/signup.html', {'form': form})


# def success(request):
#     message = messages.get_messages(request)
#     return render(request, 'signup/success.html', {'message': message})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

def success(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('signup')

    if messages.get_messages(request):
        messages.get_messages(request).used = True

    return render(request, 'signup/success.html')

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('signup')

