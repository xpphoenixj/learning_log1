# from django.urls import path, re_path, include
# from django.contrib.auth import login
#
# from . import views
#
# app_name = 'users1'
#
# urlpatterns = [
#     # login page
#     path('login/', login, {'template_name': 'users/login.html'}, name = 'login'),
#     path('logout/', views.logout_view, name="logout"),
# ]
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView
from django.conf.urls import include, url

from . import views

app_name = 'users1'

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    url(r'^register/$', views.register, name='register'),
]
