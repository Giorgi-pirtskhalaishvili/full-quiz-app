from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('profile/', views.UserDetail.as_view(), name='user'),

    path('change_password/', views.UserPasswordResetView.as_view(), name='change password')
]
