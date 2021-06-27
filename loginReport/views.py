from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
import requests
from .models import UserLogin
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
import crypt
import json



def login(request):
    from django.contrib.auth.models import User

    # user = User.objects.create_user(username='sara',
    #                                 password='$6$qFKuj17YxIW.7yMu$pklH2HQ08VdhH50NhemmThtGQY6IPOaBMv2iysOzJQVcmJ2UPSzmSLHckgDz5Obh09E8xFXF5zZHjISyE3dDs.')
    # user.save()



    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=crypt.crypt(password, '$6$' + getSalt(username)))
            print(crypt.crypt(password, '$6$' + getSalt(username)))

            if user is not None:

                ip_address = request.META.get("REMOTE_ADDR")
                user_agent = request.META['HTTP_USER_AGENT']
                referer = request.META['HTTP_REFERER']
                cookie = request.COOKIES
                ip2country = requests.get('https://ip2c.org/' + ip_address)
                country = ip2country.content

                instance = UserLogin(username=username, password=password, ip_address=ip_address, country=country,
                                     user_agent=user_agent, cookie=cookie, referer=referer, date=timezone.now())
                instance.save()

                connection_cursor = connection.cursor()

                reporter("Most Usernames",
                         "select username, count(username) from loginReport_userlogin group by username order by count(username) desc limit 10",
                         connection_cursor)
                reporter("Most Passwords",
                         "select username, count(password) from loginReport_userlogin group by username order by count(password) desc limit 10",
                         connection_cursor)
                reporter("Most User-Pass",
                         "select username,password, count(*) from loginReport_userlogin group by username,password order by count(*) desc limit 10",
                         connection_cursor)
                reporter("Most Countries",
                         "select country, count(country) from loginReport_userlogin group by country order by count(country) desc limit 10",
                         connection_cursor)

                return HttpResponse("everything was correct")


        # if form.is_valid():


    else:
        form = AuthenticationForm()

    return render(request, 'loginReport/login.html', {'form': form})


def reporter(topic, query, cursor):
    print(topic, ":")
    cursor.execute(query)
    result = cursor.fetchall()

    for record in result:
        print(record)


def getFiles(request):
    return HttpResponse("files list")


def getSalt(username):
    with open('user-pass.json') as file:
        data = json.load(file)
        salt = data[username].split('$')[2]

    return salt
