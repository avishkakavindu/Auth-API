from rest_framework import serializers
from api2.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, source='book_set')

    class Meta:
        model = Author
        fields = '__all__'
