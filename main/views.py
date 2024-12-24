from django.shortcuts import render, get_object_or_404, redirect
from . forms import DatingProfileForm, NewUserForm
from . models import DatingProfile, Interest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    return render(request, "home.html")

def datinglist(request):
    profiles = DatingProfile.objects.all()
    interests = Interest.objects.all()

    context = {
        "profiles": profiles,
        "interests": interests
    }

    return render(request, 'datinglist.html', context)

def datingprofile(request, pk):
    profile = get_object_or_404(DatingProfile, pk=pk)
    interests = Interest.objects.all()

    context = {
        "profile": profile,
        "interests": interests
    }

    return render(request, 'datingprofile.html', context)

def chatlist(request):
    return render(request, 'chatlist.html')

def profile_create(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    try:
        profile = request.user.dating_profile
        return redirect('profile_update', pk=profile.pk)
    except DatingProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = DatingProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            selected_interests = request.POST.getlist('interests')
            if selected_interests:
                profile.interests.set(Interest.objects.filter(id__in=selected_interests))
            return redirect('datingprofile', pk=profile.pk)
    else:
        form = DatingProfileForm()

    return render(request, 'create_profile.html', {'form': form})


def signup_page(request):
    if request.method == "POST":
        form = NewUserForm (request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
    'form': form
    }
    return render(request, "signup.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('datinglist')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)    

def logout_action(request):
    logout(request)
    return redirect('home_page')

def profile_update(request, pk):
    profile = get_object_or_404(DatingProfile, pk=pk, user=request.user)

    if request.method == 'POST':
        form = DatingProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            selected_interests = request.POST.getlist('interests')
            if selected_interests:
                profile.interests.set(Interest.objects.filter(id__in=selected_interests))
            return redirect('datingprofile', pk=profile.pk)
    else:
        form = DatingProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form, 'profile': profile})






