from rest_framework import routers
from .views import UserViewSet, QuoteViewSet, CommandViewSet, url_verification
from django.urls import path

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("quotes", QuoteViewSet)
router.register("commands", CommandViewSet)

app_name = 'api'
urlpatterns = [
    path('url_verification/', url_verification, name='url_verification'),
]
