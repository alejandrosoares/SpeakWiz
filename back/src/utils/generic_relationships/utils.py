from .models import ENABLED_RESOURCE_MODELS


def serialize_resources_by_type(generic_objects):
    """
    Serializes a collection of generic objects by grouping them by type and 
    converting each group into a serialized format.

    Args:
        generic_objects (iterable): A collection of generic objects to be grouped 
                                    and serialized.

    Returns:
        dict: A dictionary where the keys are the types of the generic objects 
              and the values are the serialized representations of the objects 
              in each group.
    """
    grouped_resources_by_type = group_generic_objects_by_type(generic_objects)
    serialized_resources_by_type = serialize_resources(grouped_resources_by_type)
    return serialized_resources_by_type


def group_generic_objects_by_type(generic_objects):
    """
    Formats a list of generic objects into a dictionary grouped by resource type.

    Each resource type (e.g., 'topic') is represented as a key in the dictionary, 
    and its value is a dictionary containing:
        - 'model': The model class associated with the resource type.
        - 'list_id': A list of object IDs for the resource type.
        - 'serializer': The serializer class used for the resource type.

    Args:
        generic_objects (QuerySet): A queryset of generic objects with a `content_object` attribute.

    Returns:
        dict: A dictionary where each key is a resource type (e.g., 'topic'), and the value is a dictionary 
              containing the model, list of IDs, and serializer for that resource type.

    Example:
        Input:
            [<GenericObject: Topic (id=2)>, <GenericObject: Topic (id=5)>]

        Output:
            {
                'topic': {
                    'model': <class 'topics.models.Topic'>,
                    'list_id': [2, 5],
                    'serializer': <class 'topics.serializers.TopicListSerializer'>
                }
            }
    """
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
                'serializer': ENABLED_RESOURCE_MODELS[model_name].get('serializer')
            }
    return resources


def serialize_resources(groped_resources_by_type):
    """
    Generates a list of serialized resources based on the provided formatted resources.

    Args:
        groped_resources_by_type (dict): A dictionary where each key represents a resource name, 
            and the value is another dictionary containing:
                - 'model' (Model): The Django model class associated with the resource.
                - 'serializer' (Serializer): The serializer class used to serialize the model instances.
                - 'list_id' (list): A list of primary key values to filter the model instances.

    Returns:
        list: A list of dictionaries, where each dictionary contains:
            - 'resource' (str): The name of the resource.
            - 'data' (list): A list of serialized data for the filtered model instances.
    """
    resources_list = []
    for resource_key in groped_resources_by_type.keys():
        resource = {'resource': resource_key} 
        Model = groped_resources_by_type[resource_key].get('model')
        Serializer = groped_resources_by_type[resource_key].get('serializer')
        list_id = groped_resources_by_type[resource_key].get('list_id')
        query = Model.objects.filter(pk__in=list_id)
        serialized = Serializer(query, many=True)
        resource['data'] = serialized.data
        resources_list.append(resource)
    return resources_list
