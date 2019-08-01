from django.urls import path
from .views import UserLV, UserDV, UserLikeView, UserReviewView

urlpatterns = [
    path('', UserLV.as_view(), name="users"),
    path('<user_id>/', UserDV.as_view(), name="user_detail"),
    path('<user_id>/likes', UserLikeView.as_view(), name="user_likes"),
    path('<user_id>/reviews', UserReviewView.as_view(), name="user_review")
]
