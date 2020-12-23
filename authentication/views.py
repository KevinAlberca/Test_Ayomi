from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authentication.forms import LoginForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.data.get('username'), password=form.data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error('password', 'Account not found.')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


@login_required(login_url='/login')
def home_view(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
    return render(request, 'authentication/home.html', {'user': request.user})
