from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework  import status
from django.contrib.auth.forms import UserCreationForm



#  HELP: How is this decorator working? What class is login_user a method of...?
@api_view(['POST']) # Only accepts POST requests to this method
@permission_classes([AllowAny]) # HELP: What does this do? ANSW: Got to do with IP permissions (security)
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user) # HELP: Tokens are not kept in the Postgres db, so how can I get them from Heroku instead?
        data = {
            'valid': True,
            'token': token.key
        }
    else:
        data = { 'valid': False }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        email = request.data['email'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    
    token = Token.objects.create(user=new_user) # HELP: Tokens are not kept in the Postgres db, so how can I get them from Heroku instead?
    data = { 'token': token.key }
    
    return Response(data, status=status.HTTP_201_CREATED)
