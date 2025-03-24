from rest_framework.views import APIView


from utils.generic_relationships.utils import serialize_resources_by_type
from utils.generic_relationships.views import GenericModelView
from utils.response import JsonResponseOk
from .models import Favorite
from .serializers import FavoriteSerializer


class UserFavoriteView(GenericModelView):

    generic_model = Favorite
    generic_model_serializer = FavoriteSerializer


class UserFavoriteResourceListView(APIView):

    def get(self, request):
        generic_objects = Favorite.objects.filter(
            user=request.user,
            is_active=True
        )
        serialized_resources = serialize_resources_by_type(generic_objects)
        return JsonResponseOk(serialized_resources)
