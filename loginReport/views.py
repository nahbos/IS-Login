from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("hellllllllllllllll")
    else:
        form = AuthenticationForm()

    return render(request, 'loginReport/login.html', {'form': form})
