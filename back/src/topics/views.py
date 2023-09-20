from rest_framework import generics

from .models import Topic
from .serializers import TopicListSerializer, TopicDetailSerializer


class TopicListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer


class TopicDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
