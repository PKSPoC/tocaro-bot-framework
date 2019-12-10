from rest_framework import routers
from .views import UserViewSet, QuoteViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("quotes", QuoteViewSet)
