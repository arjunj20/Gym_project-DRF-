from rest_framework import serializers
from .models import Membership, Payment
from datetime import date



class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Membership
        read_only_fields = ["user"]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Payment
        read_only_fields = ["user", "status", "created_at"]

    def validate(self, data):
        request = self.context["request"]
        user = request.user
        membership = data.get("membership")

        if not membership:
            raise serializers.ValidationError("Membership is required")

        if membership.user != user:
            raise serializers.ValidationError("You cannot pay for others")
        if membership.end_date<date.today():
            raise serializers.ValidationError("The membership has expired")
        return data
                    
            

    
        