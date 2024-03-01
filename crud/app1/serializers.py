from rest_framework import serializers
from .models import User1 
from .models import BookList
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = ['title', 'author', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ['email', 'password']