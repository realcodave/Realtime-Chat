from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    # authtoken url
    # path('api-token-auth/', obtain_auth_token, name="api_token_auth"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]
