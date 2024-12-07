from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            Profile.objects.create(user=user, name=username)
            messages.success(request, f'Your account has been created. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def edit_profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')

        if not name or not email:
            return HttpResponseBadRequest("Name and email are required.")

        user_profile.name = name
        user_profile.bio = bio
        request.user.email = email

        request.user.save()
        user_profile.save()

        return redirect('profile_view')

    return render(request, 'user/edit_profile.html', {'profile': profile})