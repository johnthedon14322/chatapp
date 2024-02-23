from django.urls import path

from room import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("login/", views.login_user, name="Login"),

]