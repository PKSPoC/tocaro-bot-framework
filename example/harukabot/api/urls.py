from rest_framework import routers
from .views import UserViewSet, QuoteViewSet, CommandViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("quotes", QuoteViewSet)
router.register("commands", CommandViewSet)
