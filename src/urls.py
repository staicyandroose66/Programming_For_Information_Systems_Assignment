from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('sign-in/',signin , name='sign-in'),
    path('add-employee/',add_employee , name='add-employee'),
    path('update-employee/<int:pk>/',update_employee , name='update-employee'),
    path('logout/',logout , name='logout'),
    path('shift-management' , shift_management , name="shift-management"),
    # Employee
    path('signin-emp/' , signin_emp , name="signin-emp"),
    path('verify-otp' , verify_otp , name="verify-otp") ,
    path('profile' , profile , name="profile"),
    path('profile-update' , profile_update , name="profile-update"),
]
