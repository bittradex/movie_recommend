from django.urls import path
from . import views

app_name = "userauths"

urlpatterns = [
    path('user/sign-up/', views.register_view, name= "sign-up"),
    path('user/sign-in/', views.login_view, name="sign-in"),
    path('account/', views.account_view, name="account"),
    path('logout', views.logout_view, name="logout"),
]
