from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
import requests


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            ip_address = request.META.get("REMOTE_ADDR")
            user_agent = request.META['HTTP_USER_AGENT']
            referer = request.META['HTTP_REFERER']
            cookie = request.COOKIES
            ip2country = requests.get('https://ip2c.org/' + ip_address)
            country = ip2country.content

            return HttpResponse("username: {} --------- password: {} ---------- IPAddress: {} --------- useragent: {} "
                                "---------- referer: {} --------- cookie: {} ---------- country: {}".format(username, password, ip_address, user_agent, referer, cookie, country))
    else:
        form = AuthenticationForm()

    return render(request, 'loginReport/login.html', {'form': form})
