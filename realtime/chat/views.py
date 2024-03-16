from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .models import CustomUser, Profile, ChatRoom, Message, Participant
from .serializers import ProfileSerializer, ChatRoomSerializer, MessageSerializer, ParticipantSerializer, UserSerializer
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html', {'user':request.user})

class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class Users(generics.ListAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        current_user = self.request.user
        queryset = CustomUser.objects.exclude(pk=current_user.pk)

        # Example: Filter users by username containing a specific keyword
        keyword = self.request.query_params.get('keyword')
        if keyword:
            queryset = queryset.filter(username__icontains=keyword)

        return queryset

@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
class UserLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ChatRoomListCreate(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
class ChatRoomRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
class CreateChatRoom(APIView):
    def post(self, request):
        # Assuming the logged-in user is the one initiating the chat
        current_user = request.user
        # Retrieve the user ID of the user being clicked
        user_id = request.data.get('user_id')
        print(current_user.id)
        print(user_id.id)
        
        # Create a chatroom between the two users
        chatroom = ChatRoom.objects.create(type='S')
        # Add participants to the chatroom
        participant1 = Participant.objects.create(user=current_user, chat_room=chatroom)
        participant2 = Participant.objects.create(user_id=user_id, chat_room=chatroom)
        
        # Return the chatroom ID or any other relevant data
        return Response({'chatroom_id': chatroom.id}, status=status.HTTP_201_CREATED)
    

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticpantRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer