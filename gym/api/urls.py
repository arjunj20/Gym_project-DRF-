from django.urls import path
from rest_framework.routers import DefaultRouter
from gym import views

router = DefaultRouter()
router.register("memberships", views.MembershipView, basename="memberships")
router.register("payments", views.PaymentView, basename="payments")

urlpatterns = router.urls