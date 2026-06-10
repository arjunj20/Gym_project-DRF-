from rest_framework import serializers
from .models import User, SumModel

import re 

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
    extra_kwargs = {
        "password": {"write_only": True}
    }# Avoiding the password at response otherwise it would shows at response 

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        user_regex = r'^[a-zA-Z0-9]+([_-]?[a-zA-Z0-9]+)*$'
        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&]).{8,}$'
        if not re.match(user_regex, username):
            raise serializers.ValidationError({"username":"Username can contains only the numbers, _ and -"})
        if not re.match(email_regex, email):
            raise serializers.ValidationError({"email": "Please enter a valid mail"})
        if not re.match(regex, password):
            raise serializers.ValidationError({
                "password": "Password must be at least 8 characters long and include a letter, number, and special character"
            })
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_owner"]
    
    
class SumSerializer(serializers.Serializer):
    num1  = serializers.IntegerField()
    num2 = serializers.IntegerField()
    

      

    