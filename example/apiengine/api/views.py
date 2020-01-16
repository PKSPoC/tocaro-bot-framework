import os

# from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Quote, Command
from .serializer import UserSerializer, QuoteSerializer, CommandSerializer


from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


class UserViewSet(viewsets.ModelViewSet):
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


@api_view(['POST'])
def url_verification(request):
    token = os.environ.get('TOCARO_TOKEN')
    if request.method == 'POST':
        received_token = request.data["token"]
        received_challenge = request.data["challenge"]
        if received_token == token and request.data["type"] == "url_verification":
            return Response({"challenge": received_challenge}, content_type="application/json")
    return Response(status=401)
