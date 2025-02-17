# Imports for hashes
from ctypes import c_uint64
from base64 import urlsafe_b64encode
# Imports for get_all_related_objects
from django.db.models.fields.related import ForeignObjectRel


def calculate_hash(input_string):

    # See https://stackoverflow.com/questions/21999983/fast-hash-for-strings
    return c_uint64(hash(input_string)).value.to_bytes(8,"big").hex()


def get_all_related_objects(instance):

    # TODO: select related for problematic fields such as deliveries and whatever our forgen equivalent is

    # init return related objects
    related_objects = []

    # iterate through all the fields of the model
    for field in instance._meta.get_fields():
        
        # check if this is foreign key
        if isinstance(field, ForeignObjectRel):

            # get the related name
            related_name = field.get_accessor_name()

            # use getattr to fetc the object
            related_instances = getattr(instance, related_name).all()

            # Add the related instances to the list
            related_objects.extend(related_instances)

            # recursviely get related objects
            for related_instance in related_instances:
                related_objects.extend(get_all_related_objects(related_instance))

    # finished
    return related_objects