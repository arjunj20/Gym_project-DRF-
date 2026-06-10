from django.urls import path
from account import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("users", views.UserView, basename="userview")
urlpatterns = [
    path("sign-up/", views.SignUp.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
] + router.urls