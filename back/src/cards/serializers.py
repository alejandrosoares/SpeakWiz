from rest_framework import serializers

from cards.models import Card


class CardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'question']


class CardDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
