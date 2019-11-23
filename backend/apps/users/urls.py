from django.urls import path
from .views import UserRegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import SellerListView, UserProfileDetailView, UserProfileUpdateView


urlpatterns = [
    path('profile/detail/', UserProfileDetailView.as_view()),
    path('profile/update/', UserProfileUpdateView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sellers/', SellerListView.as_view()),
]
