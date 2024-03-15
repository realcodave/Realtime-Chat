from django.urls import path
from django.http import HttpResponse
from . views import (
    ProfileListCreate, ProfileRetrieveUpdate,
    ChatRoomListCreate, ChatRoomRetrieveUpdate,
    MessageListCreate, MessageRetrieveUpdate,
    ParticipantListCreate, ParticpantRetrieveUpdate,
)

urlpatterns = [
    # Profile Url
    path('profile', ProfileListCreate.as_view(), name="profile-list-create"),
    path('profile/<int:pk>', ProfileRetrieveUpdate.as_view(), name="profile-retrieve-update"),
    # ChatRoom Url
    path('chatrooms/', ChatRoomListCreate.as_view(), name="chatroom-list-create"),
    path('chatrooms/<int:pk>', ChatRoomRetrieveUpdate.as_view(), name="chatroom-retrieve-update"),
    # Message Url
    path('messages/', MessageListCreate.as_view(), name="messages-list-create"),
    path('messages/<int:pk>', MessageRetrieveUpdate.as_view(), name="messages-retrieve-update"),
    # Participant Url
    path('participants/', ParticipantListCreate.as_view(), name="participants-list-create"),
    path('participants/<int:pk>', ParticpantRetrieveUpdate.as_view(), name="participants-retrieve-update"),
]