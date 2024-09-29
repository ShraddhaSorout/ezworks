from django.urls import path
from .views import SharedFileUploadView, SharedFileListView, UserRegisterView, CustomAuthToken
from .views import UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('upload/', SharedFileUploadView.as_view(), name='upload_file'),
    path('files/', SharedFileListView.as_view(), name='file_list'),
    path('users/', UserListView.as_view(), name='user_list'),
]
