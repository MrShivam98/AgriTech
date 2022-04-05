from home.models import Contact
from home.models import service
from rest_framework import serializers


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'content']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name should not be less than 3 characters!')
        return value

    def validate_email(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('email should not be less than 5 characters!')
        return value

    def validate_phone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('phone should not be less than 10 digits!')
        return value

    def validate_content(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('content should not be less than 5 characters!')
        return value


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = ['name', 'email', 'phone', 'address', 'weight', 'user', 'driveby']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name should not be less than 3 characters!')
        return value

    def validate_email(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('email should not be less than 5 characters!')
        return value

    def validate_phone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('phone should not be less than 10 digits!')
        return value

    def validate_address(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('address should not be less than 10 characters!')
        return value

    def validate_weight(self, value):
        if value > 40:
            raise serializers.ValidationError('weight should not be more than 40!')
        return value