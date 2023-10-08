from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from Register_Login import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'Bookings'

urlpatterns = [

]
