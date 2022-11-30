from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,GameSerializer,GameCreateSerializer,validate_value
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermissions,GamePermissions,UpdateBoardPermissions
from .models import Game
from rest_framework.response import Response
from rest_framework.decorators import action
import random
from rest_framework import serializers
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[UserPermissions]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        if self.request.user.is_authenticated:
            return User.objects.filter(id=self.request.user.id)
    
class GameCreateViewset(viewsets.ModelViewSet):
    serializer_class=GameCreateSerializer
    queryset=Game.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[GamePermissions]
    def list(self, request,*args, **kwargs):
        temp={"player":request.user.id}
        serializer = self.get_serializer(data=temp)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class GameViewset(viewsets.ModelViewSet):
    serializer_class=GameSerializer
    queryset=Game.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[UpdateBoardPermissions]

    def update(self, request, *args, **kwargs):
        
        validate_value(request)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if len(instance.string)>=6:
            if instance.string==instance.string[::-1]:
                return Response({"player":instance.player.username,"created_on":instance.created_on,"string":instance.string,"string_status":"max_length_reached","msg":"string is palindrome"})
            else:
                return Response({"player":instance.player.username,"created_on":instance.created_on,"string":instance.string,"string_status":"max_length_reached","msg":"string is not palindrome"})
        

        
        updated_str=instance.string+request.data["value"]+str(random.randint(0,10))

        serializer = self.get_serializer(instance, data={"string":updated_str}, partial=partial)
        
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)