from django.urls import path

from .views import *

urlpatterns = [
    path('', bills, name="all bill"),
    path('<id>', bill, name="user bill"),
]