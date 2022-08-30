from rest_framework import serializers
from profiles_api import models

class DetailsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 250)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name','password')
        extra_kwargs = { 
            'password' : {
                'write_only': True,
                'style':{'input_type':'password'}
                }
            }
    
    def create(Self, validated_data):
        user = models.UserProfile.objects.create(
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user