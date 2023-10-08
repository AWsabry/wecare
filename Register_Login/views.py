from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
# Rest Libraries
from rest_framework.response import Response
from rest_framework import status
from Register_Login.serializers import LoginSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
# Importing the utilts file

# getting csrf token
from django.middleware.csrf import get_token

# Importing Models
from Register_Login.models import Profile

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


def index(request):
    return render(request, "index.html",)

# Get CSRF Token
class get_csrf_token_api(APIView):
    def get(self,request):
        token = csrf_token = get_token(request)
        return JsonResponse({"token": token}, safe=False)
    

class create_users_API(APIView):
    def post(self,request,):
        serializer = UserSerializer(data= request.data,partial=True)
        if serializer.is_valid():
            user = Profile.objects.create_user(
                    email=request.data['email'],
                    full_name=request.data['full_name'],
                    phone_number=request.data['phone_number'],
                    password=request.data['password'],
                    age= request.data['age'],
                    weight=request.data['weight'],
                    height=request.data['height'],
                    gender=request.data['gender'],
                    goal=request.data['goal'],
                    is_active = True,
                )
            if user:
                return Response("User Created Successfully", status = status.HTTP_200_OK)
            else:
                return Response("Error Creating User", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response("Serializer Not Valid", status = status.HTTP_403_FORBIDDEN)

# Get All Users
class get_active_users(APIView):
    def get(self,request):
        all = Profile.objects.filter(is_active = True)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    
class update_user_subscription(APIView):
    def put(self,request,email):
        if request.data:
            Profile.objects.filter(is_active = True,email=email).update(subscription=True,subscription_deadline = request.data['subscription_deadline'] )
            return JsonResponse({"Message": "Subscription updated", "status" :status.HTTP_200_OK}, safe=False)
        else:
             return JsonResponse({"Message": "Subscription Not valid", "status" :status.HTTP_404_NOT_FOUND}, safe=False)



# Login Users
@csrf_protect
@api_view(['POST','GET',])
def LoginView(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_active:
                    update_last_login(None, user)
                    user_login(request, user)
                    return Response({"message": "Login successful","Names" : serializer.data,"code":status.HTTP_200_OK}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User account is not active","code":status.HTTP_403_FORBIDDEN}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"message": "Invalid credentials","code":status.HTTP_403_FORBIDDEN}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True,)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=True,status = status.HTTP_200_OK)

# Get User by Id
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class get_user_by_email(APIView):
    def get(self,request,email,*args, **kwargs):
        all = Profile.objects.filter(is_active = True,email=email)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=True,status = status.HTTP_200_OK)

    


