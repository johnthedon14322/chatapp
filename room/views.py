from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from room.models import Messages


from django.core.mail import send_mail

@login_required(login_url="/login")
def index(request):

    messages = Messages.objects.all().order_by("-id")[:5]


    # email_from = "johnthedon14322@gmail.com"
    # recipient_list = ["chichora1431@gmail.com"]
    # send_mail( "Chat Message", "email_message", email_from, recipient_list )

    return render(request, "room/index.html", {"messages": reversed(messages)})


def login_user(request):

    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
            

    return render(request, "room/login.html")