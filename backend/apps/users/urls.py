from django.urls import path
from .views import UserRegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    SellerListView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sellers/', SellerListView.as_view()),
]
