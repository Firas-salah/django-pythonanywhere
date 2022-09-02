from rest_framework import serializers   
from .models import Data

class Data_serializer(serializers.ModelSerializer):
    
    class Meta:

        model  = Data
        fields = ['id', 'created', 'title', 'content']

