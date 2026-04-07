from django.urls import include, path
from rest_framework.routers import SimpleRouter

from comments.views import CaptchaView, CommentViewSet

router = SimpleRouter()
router.register(prefix="comment", viewset=CommentViewSet, basename="comment")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/captcha/", CaptchaView.as_view()),
]
