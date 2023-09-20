from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated
from django.shortcuts import get_object_or_404

from .models import Topic, Card
from .serializers import CardListSerializer, CardDetailSerializer


class CardListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = []
    serializer_class = CardListSerializer

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        if self.is_allowed(topic.premium):
            cards = Card.objects.filter(topic=topic)
            return cards
        raise NotAuthenticated('You have to be authenticated to see this object')

    def is_allowed(self, is_premium: bool) -> bool:
        is_authenticated = self.request.user.is_authenticated
        is_premium_and_auth = is_premium and is_authenticated
        return not is_premium or is_premium_and_auth


class CardDetailView(generics.RetrieveAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = CardDetailSerializer

    def get_object(self):
        card = get_object_or_404(Card, pk=self.kwargs['card_pk'])
        return card
