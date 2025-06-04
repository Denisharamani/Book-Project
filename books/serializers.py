from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # SERIALIZER FOR BOOK TABLE
    class Meta:
        model = Book
        fields = '__all__'
