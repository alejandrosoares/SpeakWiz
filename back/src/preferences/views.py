import json

from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from .models import UserPreference
from .serializers import UserPreferenceSerializer
from .utils import (
    get_enabled_model_from,
    update_user_preference
)


class UserPreferenceView(APIView):

    def get(self, request):
        user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
        data = UserPreferenceSerializer(user_preference)
        return JsonResponse(data.data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            model = get_enabled_model_from(data.get('resourceType'))
            resource = model.objects.get(id=data.get('resourceId'))
            feedback = data.get('resourceValue')
        except (json.decoder.JSONDecodeError, ValueError, AttributeError):
            return JsonResponse(
                'BAD_REQUEST',
                status=status.HTTP_400_BAD_REQUEST,
                safe=False)
        else:
            update_user_preference(resource, feedback, request.user)

        return JsonResponse('OK', status=status.HTTP_201_CREATED, safe=False)
