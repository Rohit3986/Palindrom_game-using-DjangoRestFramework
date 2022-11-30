from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Game

#------------- validation for value-----------------
def validate_value(request):
    if not "value" in request.data.keys() or len(request.data)>1:
        raise serializers.ValidationError("only value field is updatable")
    value=request.data.get("value")
    print("value is ",value)
    if not value.isalpha() or value!=value.lower() or len(value)>1:
        raise serializers.ValidationError("value should be lie between a-z only and only one character is allowed")
#-------------------------------------------------

class UserSerializer(serializers.HyperlinkedModelSerializer):
    confirm_password= serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","confirm_password","url"]
        extra_kwargs = {'password': {'write_only': True,'style':{'input_type':'password'}}}
    def validate(self, data):
        password=data.get("password",None)
        confirm_password=data.get("confirm_password",None)
        if password:
            if password!=confirm_password:
                raise serializers.ValidationError("password should be match with confirm password")
            data['password']=make_password(data['password'])
            data.pop("confirm_password")
        return data

class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Game
        fields=["player","string","created_on"]
        


class GameSerializer(serializers.ModelSerializer):
    value=serializers.CharField(max_length=1, write_only=True)
    class Meta:
        model=Game
        fields=["player","string","created_on","value"]
        extra_kwargs = {'player': {'read_only': True}}
        def validate(self, data):
            print("hii")
            data.pop("value")
            return data

    