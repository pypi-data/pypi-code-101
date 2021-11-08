'''
# AWS CDK CloudFormation Constructs for TF::AD::User

CloudFormation equivalent of ad_user

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-User/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


class CfnUser(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-ad-user.CfnUser",
):
    '''A CloudFormation ``TF::AD::User``.

    :cloudformationResource: TF::AD::User
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[builtins.bool] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[builtins.bool] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``TF::AD::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: 
        :param principal_name: 
        :param sam_account_name: 
        :param cannot_change_password: 
        :param city: 
        :param company: 
        :param container: 
        :param country: 
        :param custom_attributes: 
        :param department: 
        :param description: 
        :param division: 
        :param email_address: 
        :param employee_id: 
        :param employee_number: 
        :param enabled: 
        :param fax: 
        :param given_name: 
        :param home_directory: 
        :param home_drive: 
        :param home_page: 
        :param home_phone: 
        :param initial_password: 
        :param initials: 
        :param mobile_phone: 
        :param office: 
        :param office_phone: 
        :param organization: 
        :param other_name: 
        :param password_never_expires: 
        :param po_box: 
        :param postal_code: 
        :param smart_card_logon_required: 
        :param state: 
        :param street_address: 
        :param surname: 
        :param title: 
        :param trusted_for_delegation: 
        '''
        props = CfnUserProps(
            display_name=display_name,
            principal_name=principal_name,
            sam_account_name=sam_account_name,
            cannot_change_password=cannot_change_password,
            city=city,
            company=company,
            container=container,
            country=country,
            custom_attributes=custom_attributes,
            department=department,
            description=description,
            division=division,
            email_address=email_address,
            employee_id=employee_id,
            employee_number=employee_number,
            enabled=enabled,
            fax=fax,
            given_name=given_name,
            home_directory=home_directory,
            home_drive=home_drive,
            home_page=home_page,
            home_phone=home_phone,
            initial_password=initial_password,
            initials=initials,
            mobile_phone=mobile_phone,
            office=office,
            office_phone=office_phone,
            organization=organization,
            other_name=other_name,
            password_never_expires=password_never_expires,
            po_box=po_box,
            postal_code=postal_code,
            smart_card_logon_required=smart_card_logon_required,
            state=state,
            street_address=street_address,
            surname=surname,
            title=title,
            trusted_for_delegation=trusted_for_delegation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AD::User.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSid")
    def attr_sid(self) -> builtins.str:
        '''Attribute ``TF::AD::User.Sid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AD::User.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-ad-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "principal_name": "principalName",
        "sam_account_name": "samAccountName",
        "cannot_change_password": "cannotChangePassword",
        "city": "city",
        "company": "company",
        "container": "container",
        "country": "country",
        "custom_attributes": "customAttributes",
        "department": "department",
        "description": "description",
        "division": "division",
        "email_address": "emailAddress",
        "employee_id": "employeeId",
        "employee_number": "employeeNumber",
        "enabled": "enabled",
        "fax": "fax",
        "given_name": "givenName",
        "home_directory": "homeDirectory",
        "home_drive": "homeDrive",
        "home_page": "homePage",
        "home_phone": "homePhone",
        "initial_password": "initialPassword",
        "initials": "initials",
        "mobile_phone": "mobilePhone",
        "office": "office",
        "office_phone": "officePhone",
        "organization": "organization",
        "other_name": "otherName",
        "password_never_expires": "passwordNeverExpires",
        "po_box": "poBox",
        "postal_code": "postalCode",
        "smart_card_logon_required": "smartCardLogonRequired",
        "state": "state",
        "street_address": "streetAddress",
        "surname": "surname",
        "title": "title",
        "trusted_for_delegation": "trustedForDelegation",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[builtins.bool] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[builtins.bool] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''CloudFormation equivalent of ad_user.

        :param display_name: 
        :param principal_name: 
        :param sam_account_name: 
        :param cannot_change_password: 
        :param city: 
        :param company: 
        :param container: 
        :param country: 
        :param custom_attributes: 
        :param department: 
        :param description: 
        :param division: 
        :param email_address: 
        :param employee_id: 
        :param employee_number: 
        :param enabled: 
        :param fax: 
        :param given_name: 
        :param home_directory: 
        :param home_drive: 
        :param home_page: 
        :param home_phone: 
        :param initial_password: 
        :param initials: 
        :param mobile_phone: 
        :param office: 
        :param office_phone: 
        :param organization: 
        :param other_name: 
        :param password_never_expires: 
        :param po_box: 
        :param postal_code: 
        :param smart_card_logon_required: 
        :param state: 
        :param street_address: 
        :param surname: 
        :param title: 
        :param trusted_for_delegation: 

        :schema: CfnUserProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "principal_name": principal_name,
            "sam_account_name": sam_account_name,
        }
        if cannot_change_password is not None:
            self._values["cannot_change_password"] = cannot_change_password
        if city is not None:
            self._values["city"] = city
        if company is not None:
            self._values["company"] = company
        if container is not None:
            self._values["container"] = container
        if country is not None:
            self._values["country"] = country
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if department is not None:
            self._values["department"] = department
        if description is not None:
            self._values["description"] = description
        if division is not None:
            self._values["division"] = division
        if email_address is not None:
            self._values["email_address"] = email_address
        if employee_id is not None:
            self._values["employee_id"] = employee_id
        if employee_number is not None:
            self._values["employee_number"] = employee_number
        if enabled is not None:
            self._values["enabled"] = enabled
        if fax is not None:
            self._values["fax"] = fax
        if given_name is not None:
            self._values["given_name"] = given_name
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_drive is not None:
            self._values["home_drive"] = home_drive
        if home_page is not None:
            self._values["home_page"] = home_page
        if home_phone is not None:
            self._values["home_phone"] = home_phone
        if initial_password is not None:
            self._values["initial_password"] = initial_password
        if initials is not None:
            self._values["initials"] = initials
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if office is not None:
            self._values["office"] = office
        if office_phone is not None:
            self._values["office_phone"] = office_phone
        if organization is not None:
            self._values["organization"] = organization
        if other_name is not None:
            self._values["other_name"] = other_name
        if password_never_expires is not None:
            self._values["password_never_expires"] = password_never_expires
        if po_box is not None:
            self._values["po_box"] = po_box
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if smart_card_logon_required is not None:
            self._values["smart_card_logon_required"] = smart_card_logon_required
        if state is not None:
            self._values["state"] = state
        if street_address is not None:
            self._values["street_address"] = street_address
        if surname is not None:
            self._values["surname"] = surname
        if title is not None:
            self._values["title"] = title
        if trusted_for_delegation is not None:
            self._values["trusted_for_delegation"] = trusted_for_delegation

    @builtins.property
    def display_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#DisplayName
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#PrincipalName
        '''
        result = self._values.get("principal_name")
        assert result is not None, "Required property 'principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sam_account_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#SamAccountName
        '''
        result = self._values.get("sam_account_name")
        assert result is not None, "Required property 'sam_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cannot_change_password(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#CannotChangePassword
        '''
        result = self._values.get("cannot_change_password")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#City
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Company
        '''
        result = self._values.get("company")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Country
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_attributes(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#CustomAttributes
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Department
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def division(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Division
        '''
        result = self._values.get("division")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmailAddress
        '''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmployeeId
        '''
        result = self._values.get("employee_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_number(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmployeeNumber
        '''
        result = self._values.get("employee_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Fax
        '''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#GivenName
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomeDirectory
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_drive(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomeDrive
        '''
        result = self._values.get("home_drive")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_page(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomePage
        '''
        result = self._values.get("home_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomePhone
        '''
        result = self._values.get("home_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_password(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#InitialPassword
        '''
        result = self._values.get("initial_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initials(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Initials
        '''
        result = self._values.get("initials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#MobilePhone
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Office
        '''
        result = self._values.get("office")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#OfficePhone
        '''
        result = self._values.get("office_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Organization
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def other_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#OtherName
        '''
        result = self._values.get("other_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_never_expires(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#PasswordNeverExpires
        '''
        result = self._values.get("password_never_expires")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def po_box(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#PoBox
        '''
        result = self._values.get("po_box")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#PostalCode
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smart_card_logon_required(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#SmartCardLogonRequired
        '''
        result = self._values.get("smart_card_logon_required")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#State
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#StreetAddress
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Surname
        '''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trusted_for_delegation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#TrustedForDelegation
        '''
        result = self._values.get("trusted_for_delegation")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUser",
    "CfnUserProps",
]

publication.publish()
