from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileEditForm
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            Profile.objects.create(user=user, name=f'{user.first_name} {user.last_name}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def edit_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'user/profile-edit.html', {'form': form})