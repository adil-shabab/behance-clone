from .models import Profile
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
# Create your views here.




def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
        else:
            return redirect('signup')
    context = {'form': form}
    return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("No user found")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')




    return render(request, 'signin.html')

 

def logout(request):
    django_logout(request)
    return redirect('signin')


def other_profile(request, pk):
    profile = Profile.objects.get(id = pk)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

def userAccount(request):
    profile = request.user.profile
    works = profile.work_set.all()


    context = {'profile':profile, 'works': works}

    return render(request, 'profile.html', context)