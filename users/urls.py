from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import users, user, owners, owner

urlpatterns = [
    path('users', users, name="all users"),
    path('user/<id>', user, name="single user"),
    path('owners', owners ,name="all owner"),
    path('owner/<id>', owner, name="single owner"),
    path('gettoken', obtain_auth_token),
]