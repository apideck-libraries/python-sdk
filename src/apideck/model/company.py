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
    from apideck.model.address import Address
    from apideck.model.bank_account import BankAccount
    from apideck.model.company_row_type import CompanyRowType
    from apideck.model.currency import Currency
    from apideck.model.custom_field import CustomField
    from apideck.model.custom_mappings import CustomMappings
    from apideck.model.email import Email
    from apideck.model.pass_through_body import PassThroughBody
    from apideck.model.phone_number import PhoneNumber
    from apideck.model.social_link import SocialLink
    from apideck.model.tags import Tags
    from apideck.model.website import Website
    globals()['Address'] = Address
    globals()['BankAccount'] = BankAccount
    globals()['CompanyRowType'] = CompanyRowType
    globals()['Currency'] = Currency
    globals()['CustomField'] = CustomField
    globals()['CustomMappings'] = CustomMappings
    globals()['Email'] = Email
    globals()['PassThroughBody'] = PassThroughBody
    globals()['PhoneNumber'] = PhoneNumber
    globals()['SocialLink'] = SocialLink
    globals()['Tags'] = Tags
    globals()['Website'] = Website


class Company(ModelNormal):
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
    }

    validations = {
    }

    additional_properties_type = None

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
            'name': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'interaction_count': (int, none_type,),  # noqa: E501
            'owner_id': (str, none_type,),  # noqa: E501
            'image': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'vat_number': (str, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'fax': (str, none_type,),  # noqa: E501
            'annual_revenue': (str, none_type,),  # noqa: E501
            'number_of_employees': (str, none_type,),  # noqa: E501
            'industry': (str, none_type,),  # noqa: E501
            'ownership': (str, none_type,),  # noqa: E501
            'sales_tax_number': (str, none_type,),  # noqa: E501
            'payee_number': (str, none_type,),  # noqa: E501
            'abn_or_tfn': (str, none_type,),  # noqa: E501
            'abn_branch': (str, none_type,),  # noqa: E501
            'acn': (str, none_type,),  # noqa: E501
            'first_name': (str, none_type,),  # noqa: E501
            'last_name': (str, none_type,),  # noqa: E501
            'parent_id': (str, none_type,),  # noqa: E501
            'bank_accounts': ([BankAccount],),  # noqa: E501
            'websites': ([Website],),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'social_links': ([SocialLink],),  # noqa: E501
            'phone_numbers': ([PhoneNumber],),  # noqa: E501
            'emails': ([Email],),  # noqa: E501
            'row_type': (CompanyRowType,),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'read_only': (bool, none_type,),  # noqa: E501
            'last_activity_at': (datetime, none_type,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'salutation': (str, none_type,),  # noqa: E501
            'birthday': (date, none_type,),  # noqa: E501
            'custom_mappings': (CustomMappings,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'pass_through': (PassThroughBody,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'id': 'id',  # noqa: E501
        'interaction_count': 'interaction_count',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'image': 'image',  # noqa: E501
        'description': 'description',  # noqa: E501
        'vat_number': 'vat_number',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'status': 'status',  # noqa: E501
        'fax': 'fax',  # noqa: E501
        'annual_revenue': 'annual_revenue',  # noqa: E501
        'number_of_employees': 'number_of_employees',  # noqa: E501
        'industry': 'industry',  # noqa: E501
        'ownership': 'ownership',  # noqa: E501
        'sales_tax_number': 'sales_tax_number',  # noqa: E501
        'payee_number': 'payee_number',  # noqa: E501
        'abn_or_tfn': 'abn_or_tfn',  # noqa: E501
        'abn_branch': 'abn_branch',  # noqa: E501
        'acn': 'acn',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'bank_accounts': 'bank_accounts',  # noqa: E501
        'websites': 'websites',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'social_links': 'social_links',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'row_type': 'row_type',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'read_only': 'read_only',  # noqa: E501
        'last_activity_at': 'last_activity_at',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'salutation': 'salutation',  # noqa: E501
        'birthday': 'birthday',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'pass_through': 'pass_through',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'interaction_count',  # noqa: E501
        'parent_id',  # noqa: E501
        'last_activity_at',  # noqa: E501
        'deleted',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """Company - a model defined in OpenAPI

        Args:
            name (str, none_type): Name of the company

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
            id (str): Unique identifier for the company. [optional]  # noqa: E501
            interaction_count (int, none_type): Number of interactions. [optional]  # noqa: E501
            owner_id (str, none_type): Owner ID. [optional]  # noqa: E501
            image (str, none_type): The Image URL of the company. [optional]  # noqa: E501
            description (str, none_type): A description of the company. [optional]  # noqa: E501
            vat_number (str, none_type): The VAT number of the company. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            status (str, none_type): The status of the company. [optional]  # noqa: E501
            fax (str, none_type): The fax number of the company. [optional]  # noqa: E501
            annual_revenue (str, none_type): The annual revenue of the company. [optional]  # noqa: E501
            number_of_employees (str, none_type): Number of employees. [optional]  # noqa: E501
            industry (str, none_type): The industry represents the type of business the company is in.. [optional]  # noqa: E501
            ownership (str, none_type): The ownership indicates the type of ownership of the company.. [optional]  # noqa: E501
            sales_tax_number (str, none_type): A sales tax number is a unique number that identifies a company for tax purposes.. [optional]  # noqa: E501
            payee_number (str, none_type): A payee number is a unique number that identifies a payee for tax purposes.. [optional]  # noqa: E501
            abn_or_tfn (str, none_type): An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.. [optional]  # noqa: E501
            abn_branch (str, none_type): An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.. [optional]  # noqa: E501
            acn (str, none_type): The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.. [optional]  # noqa: E501
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            parent_id (str, none_type): Parent ID. [optional]  # noqa: E501
            bank_accounts ([BankAccount]): [optional]  # noqa: E501
            websites ([Website]): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            social_links ([SocialLink]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            row_type (CompanyRowType): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            read_only (bool, none_type): Whether the company is read-only or not. [optional]  # noqa: E501
            last_activity_at (datetime, none_type): Last activity date. [optional]  # noqa: E501
            deleted (bool): Whether the company is deleted or not. [optional]  # noqa: E501
            salutation (str, none_type): A formal salutation for the person. For example, 'Mr', 'Mrs'. [optional]  # noqa: E501
            birthday (date, none_type): The date of birth of the person.. [optional]  # noqa: E501
            custom_mappings (CustomMappings): [optional]  # noqa: E501
            updated_by (str, none_type): Updated by user ID. [optional]  # noqa: E501
            created_by (str, none_type): Created by user ID. [optional]  # noqa: E501
            updated_at (datetime, none_type): Last updated date. [optional]  # noqa: E501
            created_at (datetime, none_type): Creation date. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
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

        self.name = name
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
    def __init__(self, name, *args, **kwargs):  # noqa: E501
        """Company - a model defined in OpenAPI

        Args:
            name (str, none_type): Name of the company

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
            id (str): Unique identifier for the company. [optional]  # noqa: E501
            interaction_count (int, none_type): Number of interactions. [optional]  # noqa: E501
            owner_id (str, none_type): Owner ID. [optional]  # noqa: E501
            image (str, none_type): The Image URL of the company. [optional]  # noqa: E501
            description (str, none_type): A description of the company. [optional]  # noqa: E501
            vat_number (str, none_type): The VAT number of the company. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            status (str, none_type): The status of the company. [optional]  # noqa: E501
            fax (str, none_type): The fax number of the company. [optional]  # noqa: E501
            annual_revenue (str, none_type): The annual revenue of the company. [optional]  # noqa: E501
            number_of_employees (str, none_type): Number of employees. [optional]  # noqa: E501
            industry (str, none_type): The industry represents the type of business the company is in.. [optional]  # noqa: E501
            ownership (str, none_type): The ownership indicates the type of ownership of the company.. [optional]  # noqa: E501
            sales_tax_number (str, none_type): A sales tax number is a unique number that identifies a company for tax purposes.. [optional]  # noqa: E501
            payee_number (str, none_type): A payee number is a unique number that identifies a payee for tax purposes.. [optional]  # noqa: E501
            abn_or_tfn (str, none_type): An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.. [optional]  # noqa: E501
            abn_branch (str, none_type): An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.. [optional]  # noqa: E501
            acn (str, none_type): The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.. [optional]  # noqa: E501
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            parent_id (str, none_type): Parent ID. [optional]  # noqa: E501
            bank_accounts ([BankAccount]): [optional]  # noqa: E501
            websites ([Website]): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            social_links ([SocialLink]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            row_type (CompanyRowType): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            read_only (bool, none_type): Whether the company is read-only or not. [optional]  # noqa: E501
            last_activity_at (datetime, none_type): Last activity date. [optional]  # noqa: E501
            deleted (bool): Whether the company is deleted or not. [optional]  # noqa: E501
            salutation (str, none_type): A formal salutation for the person. For example, 'Mr', 'Mrs'. [optional]  # noqa: E501
            birthday (date, none_type): The date of birth of the person.. [optional]  # noqa: E501
            custom_mappings (CustomMappings): [optional]  # noqa: E501
            updated_by (str, none_type): Updated by user ID. [optional]  # noqa: E501
            created_by (str, none_type): Created by user ID. [optional]  # noqa: E501
            updated_at (datetime, none_type): Last updated date. [optional]  # noqa: E501
            created_at (datetime, none_type): Creation date. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
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

        self.name = name
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
