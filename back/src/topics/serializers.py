from rest_framework import serializers

from cards.models import Topic


class TopicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ['id', 'title', 'enable', 'premium', 'description']


class TopicDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
