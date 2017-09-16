from rest_framework import serializers

from models import List, Card


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List,
        fields = ('title', 'order', 'id')


class CardSerializer(serializers.ModelSerializer):
    listId = serializers.PrimaryKeyRelatedField(queryset=List.objects.all())

    class Meta:
        model = Card,
        fields = ('title', 'description', 'listId', 'id')

