from rest_framework.views import APIView

from utils.models.generics import ENABLED_RESOURCE_MODELS
from utils.views import GenericModelView
from utils.response import JsonResponseOk
from .models import Favorite
from .serializers import FavoriteSerializer


class UserFavoriteView(GenericModelView):

    generic_model = Favorite
    generic_model_serializer = FavoriteSerializer


class UserFavoriteResourceListView(APIView):

    enabled_models = ENABLED_RESOURCE_MODELS

    def get(self, request):
        user = request.user
        generic_objects = Favorite.objects.filter(
            user=user,
            is_active=True
        )
        formatted_resources = self.__get_formatted_resources_by_resource_type(
            generic_objects)
        serialized_resources = self.__get_serialized_resources_list(formatted_resources)
        return JsonResponseOk(serialized_resources)

    def __get_formatted_resources_by_resource_type(self, generic_objects):
        resources = {}
        for generic in generic_objects:
            model = generic.content_object.__class__
            model_name = model.__name__.lower()
            if resources.get(model_name):
                list_id = resources[model_name].get('list_id', [])
                list_id.append(generic.object_id)
            else:
                resources[model_name] = {
                    'model': model,
                    'list_id': [generic.object_id],
                    'serializer': self.enabled_models[model_name].get('serializer')
                }
        return resources

    def __get_serialized_resources_list(self, formatted_resources):
        resources_list = []
        for resource_key in formatted_resources.keys():
            Model = formatted_resources[resource_key].get('model')
            Serializer = formatted_resources[resource_key].get('serializer')
            list_id = formatted_resources[resource_key].get('list_id')
            query = Model.objects.filter(pk__in=list_id)
            serialized = Serializer(query, many=True)
            resources_list.append(serialized.data)
        return resources_list
