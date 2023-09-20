from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType

from json import loads
from json.decoder import JSONDecodeError

from utils.models.generics import ENABLED_RESOURCE_MODELS
from utils.response import (
    JsonResponseOk,
    JsonResponseCreated,
    JsonResponseBadRequest
)


def get_data_from(request_body: bytes) -> dict:
    """Deserializes request body.
    JSONDecodeError is raised if this method cannot deserialize the argument.
    """
    data = loads(request_body)
    return data


class GenericModelView(APIView):
    """
    Base class to work with generic relationships.
    You have to define which generic models and its serializer you want work with

    Operations:
    - get all
    - get by resource type and resource if
    - create or update existent
    - delete: soft deletion. It marks the generic obj has disabled

    generic_obj: is the instance of the generic_model
    resource_obj: is the instance with generic relationship with the generic model
    """
    enabled_models = ENABLED_RESOURCE_MODELS
    generic_model = None
    generic_model_serializer = None

    def get(self, request):

        if request.query_params:
            try:
                generic_obj = self.__get_single_generic_obj(request)
            except AttributeError:
                response = JsonResponseBadRequest()
            except self.generic_model.DoesNotExist:
                response = JsonResponseOk()
            else:
                data = self.generic_model_serializer(generic_obj)
                response = JsonResponseOk(data.data)
        else:
            generic_objects = self.generic_model.objects.filter(
                user=request.user,
                is_active=True
            )
            data = self.generic_model_serializer(generic_objects, many=True)
            response = JsonResponseOk(data.data)
        return response

    def post(self, request):
        try:
            data = get_data_from(request.body)
            resource_type = data.get('resourceType')
            resource_id = data.get('resourceId')
            resource_obj = self.__get_resource_obj(resource_type, resource_id)
        except (JSONDecodeError, ValueError, AttributeError):
            response = JsonResponseBadRequest()
        else:
            generic_obj = self.__create_or_active_existent(resource_obj, request.user)
            data = self.generic_model_serializer(generic_obj)
            response = JsonResponseCreated(data.data)
        return response

    def delete(self, request):
        try:
            resource_id = request.GET.get('resourceId')
            self.generic_model.objects.filter(id=resource_id).update(is_active=False)
        except AttributeError:
            response = JsonResponseBadRequest()
        else:
            response = JsonResponseOk()
        return response

    def __get_single_generic_obj(self, request):
        resource_type = request.GET.get('resourceType')
        resource_id = request.GET.get('resourceId')
        resource_obj = self.__get_resource_obj(resource_type, resource_id)
        generic_obj = self.__get_generic_obj(
            resource=resource_obj,
            user=request.user,
            is_active=True
        )
        return generic_obj

    def __create_or_active_existent(self, resource_obj, user):
        try:
            generic_obj = self.__get_generic_obj(resource_obj, user)
        except self.generic_model.DoesNotExist:
            generic_obj = self.generic_model.objects.create(
                user=user, content_object=resource_obj)
        else:
            generic_obj.is_active = True
            generic_obj.save()
        return generic_obj

    def __get_resource_obj(self, resource_type, resource_id):
        Model = self.__get_enabled_resource_model(resource_type)
        resource_obj = Model.objects.get(id=resource_id)
        return resource_obj

    def __get_generic_obj(self, resource, user, is_active=False):
        model_name = resource.__class__.__name__.lower()
        content_type = self.__get_content_type(model_name)
        generic_obj = self.generic_model.objects.get(
            object_id=resource.id,
            content_type=content_type,
            user=user,
            is_active=is_active
        )
        return generic_obj

    def __get_content_type(self, model_name):
        Model = self.__get_enabled_resource_model(model_name)
        content_type = ContentType.objects.get_for_model(Model)
        return content_type

    def __get_enabled_resource_model(self, model_name):
        Model = self.enabled_models.get(model_name).get('model')
        return Model
