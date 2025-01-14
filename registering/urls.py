from django.urls import path
from registering.views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserViewAPI,
    UserLogoutViewAPI,
    UserDetailAPIView,
    UserUpdateAPIViewEditProfile,
    UserUpdateAPIViewFavorites,
    UserDetailAPIViewEditProfile,
    UserDetailAPIViewFavorites,
    CreateGalleryAPIView,
    ListGalleriesAPIView,
)

urlpatterns = [
    path('user/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('user/login/', UserLoginAPIView.as_view(), name='login'),
    path('user/', UserViewAPI.as_view()),
    path('user/logout/', UserLogoutViewAPI.as_view()),
    path('user/<int:user_id>/detail/', UserDetailAPIView.as_view()), 
    path('user/<int:user_id>/updateEditProfile/', UserUpdateAPIViewEditProfile.as_view()),
    path('user/<int:user_id>/updateFavorites/',  UserUpdateAPIViewFavorites.as_view()),
    path('user/<int:user_id>/detailEditProfile/',  UserDetailAPIViewEditProfile.as_view()), 
    path('user/<int:user_id>/detailFavorites/', UserDetailAPIViewFavorites.as_view()), 
    path('gallery/create/', CreateGalleryAPIView.as_view(), name='create-gallery'),
    path('galleries/', ListGalleriesAPIView.as_view(), name='list-galleries'),
]
