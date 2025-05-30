"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.17.2
    Contact: support@apideck.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from apideck.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from apideck.exceptions import ApiAttributeError


def lazy_import():
    from apideck.model.order_pickup_details_curbside_pickup_details import OrderPickupDetailsCurbsidePickupDetails
    from apideck.model.order_pickup_details_recipient import OrderPickupDetailsRecipient
    globals()['OrderPickupDetailsCurbsidePickupDetails'] = OrderPickupDetailsCurbsidePickupDetails
    globals()['OrderPickupDetailsRecipient'] = OrderPickupDetailsRecipient


class OrderPickupDetails(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('schedule_type',): {
            'SCHEDULED': "scheduled",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'accepted_at': (datetime, none_type,),  # noqa: E501
            'auto_complete_duration': (str, none_type,),  # noqa: E501
            'cancel_reason': (str, none_type,),  # noqa: E501
            'expires_at': (datetime,),  # noqa: E501
            'schedule_type': (str,),  # noqa: E501
            'pickup_at': (datetime,),  # noqa: E501
            'pickup_window_duration': (str,),  # noqa: E501
            'prep_time_duration': (str,),  # noqa: E501
            'note': (str,),  # noqa: E501
            'placed_at': (datetime,),  # noqa: E501
            'rejected_at': (datetime,),  # noqa: E501
            'ready_at': (datetime,),  # noqa: E501
            'expired_at': (datetime,),  # noqa: E501
            'picked_up_at': (datetime,),  # noqa: E501
            'canceled_at': (datetime,),  # noqa: E501
            'is_curbside_pickup': (bool,),  # noqa: E501
            'curbside_pickup_details': (OrderPickupDetailsCurbsidePickupDetails,),  # noqa: E501
            'recipient': (OrderPickupDetailsRecipient,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'accepted_at': 'accepted_at',  # noqa: E501
        'auto_complete_duration': 'auto_complete_duration',  # noqa: E501
        'cancel_reason': 'cancel_reason',  # noqa: E501
        'expires_at': 'expires_at',  # noqa: E501
        'schedule_type': 'schedule_type',  # noqa: E501
        'pickup_at': 'pickup_at',  # noqa: E501
        'pickup_window_duration': 'pickup_window_duration',  # noqa: E501
        'prep_time_duration': 'prep_time_duration',  # noqa: E501
        'note': 'note',  # noqa: E501
        'placed_at': 'placed_at',  # noqa: E501
        'rejected_at': 'rejected_at',  # noqa: E501
        'ready_at': 'ready_at',  # noqa: E501
        'expired_at': 'expired_at',  # noqa: E501
        'picked_up_at': 'picked_up_at',  # noqa: E501
        'canceled_at': 'canceled_at',  # noqa: E501
        'is_curbside_pickup': 'is_curbside_pickup',  # noqa: E501
        'curbside_pickup_details': 'curbside_pickup_details',  # noqa: E501
        'recipient': 'recipient',  # noqa: E501
    }

    read_only_vars = {
        'accepted_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """OrderPickupDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            accepted_at (datetime, none_type): [optional]  # noqa: E501
            auto_complete_duration (str, none_type): The duration of time after which an open and accepted pickup fulfillment is automatically moved to the COMPLETED state. The duration must be in RFC 3339 format (for example, 'P1W3D').. [optional]  # noqa: E501
            cancel_reason (str, none_type): A description of why the pickup was canceled.. [optional]  # noqa: E501
            expires_at (datetime): Indicating when this fulfillment expires if it is not accepted. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\"). The expiration time can only be set up to 7 days in the future. If `expires_at` is not set, this pickup fulfillment is automatically accepted when  placed.. [optional]  # noqa: E501
            schedule_type (str): The schedule type of the pickup fulfillment.. [optional] if omitted the server will use the default value of "scheduled"  # noqa: E501
            pickup_at (datetime): The timestamp that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,  \"2016-09-04T23:59:33.123Z\".  For fulfillments with the schedule type `ASAP`, this is automatically set to the current time plus the expected duration to prepare the fulfillment.. [optional]  # noqa: E501
            pickup_window_duration (str): The window of time in which the order should be picked up after the `pickup_at` timestamp. Must be in RFC 3339 duration format, e.g., \"P1W3D\". Can be used as an informational guideline for merchants.. [optional]  # noqa: E501
            prep_time_duration (str): The duration of time it takes to prepare this fulfillment. The duration must be in RFC 3339 format (for example, \"P1W3D\").. [optional]  # noqa: E501
            note (str): A note meant to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale application and set by the API.. [optional]  # noqa: E501
            placed_at (datetime): Indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            rejected_at (datetime): Indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            ready_at (datetime): Indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            expired_at (datetime): Indicating when the fulfillment expired. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            picked_up_at (datetime): Indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            canceled_at (datetime): Indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            is_curbside_pickup (bool): If set to `true`, indicates that this pickup order is for curbside pickup, not in-store pickup.. [optional]  # noqa: E501
            curbside_pickup_details (OrderPickupDetailsCurbsidePickupDetails): [optional]  # noqa: E501
            recipient (OrderPickupDetailsRecipient): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """OrderPickupDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            accepted_at (datetime, none_type): [optional]  # noqa: E501
            auto_complete_duration (str, none_type): The duration of time after which an open and accepted pickup fulfillment is automatically moved to the COMPLETED state. The duration must be in RFC 3339 format (for example, 'P1W3D').. [optional]  # noqa: E501
            cancel_reason (str, none_type): A description of why the pickup was canceled.. [optional]  # noqa: E501
            expires_at (datetime): Indicating when this fulfillment expires if it is not accepted. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\"). The expiration time can only be set up to 7 days in the future. If `expires_at` is not set, this pickup fulfillment is automatically accepted when  placed.. [optional]  # noqa: E501
            schedule_type (str): The schedule type of the pickup fulfillment.. [optional] if omitted the server will use the default value of "scheduled"  # noqa: E501
            pickup_at (datetime): The timestamp that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,  \"2016-09-04T23:59:33.123Z\".  For fulfillments with the schedule type `ASAP`, this is automatically set to the current time plus the expected duration to prepare the fulfillment.. [optional]  # noqa: E501
            pickup_window_duration (str): The window of time in which the order should be picked up after the `pickup_at` timestamp. Must be in RFC 3339 duration format, e.g., \"P1W3D\". Can be used as an informational guideline for merchants.. [optional]  # noqa: E501
            prep_time_duration (str): The duration of time it takes to prepare this fulfillment. The duration must be in RFC 3339 format (for example, \"P1W3D\").. [optional]  # noqa: E501
            note (str): A note meant to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale application and set by the API.. [optional]  # noqa: E501
            placed_at (datetime): Indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            rejected_at (datetime): Indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            ready_at (datetime): Indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            expired_at (datetime): Indicating when the fulfillment expired. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            picked_up_at (datetime): Indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            canceled_at (datetime): Indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").. [optional]  # noqa: E501
            is_curbside_pickup (bool): If set to `true`, indicates that this pickup order is for curbside pickup, not in-store pickup.. [optional]  # noqa: E501
            curbside_pickup_details (OrderPickupDetailsCurbsidePickupDetails): [optional]  # noqa: E501
            recipient (OrderPickupDetailsRecipient): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
