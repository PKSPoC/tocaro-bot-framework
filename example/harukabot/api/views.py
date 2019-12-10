from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import User, Quote, Command
from .serializer import UserSerializer, QuoteSerializer, CommandSerializer


# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer


#    @method_decorator(csrf_exempt)
#    def dispatch(self, *args, **kwargs):
#        return super(UserViewSet, self).dispatch(*args, **kwargs)


class QuoteViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    filter_fields = ("author", "status", "id")


class CommandViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
