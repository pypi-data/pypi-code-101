'''
# AWS CDK CloudFormation Constructs for TF::AzureAD::User

Manages a User within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/azuread/TF-AzureAD-User/docs/README.md)
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
    jsii_type="@cdk-cloudformation/tf-azuread-user.CfnUser",
):
    '''A CloudFormation ``TF::AzureAD::User``.

    :cloudformationResource: TF::AzureAD::User
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        password: builtins.str,
        user_principal_name: builtins.str,
        account_enabled: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        force_password_change: typing.Optional[builtins.bool] = None,
        given_name: typing.Optional[builtins.str] = None,
        immutable_id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        mobile: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office_location: typing.Optional[builtins.str] = None,
        onpremises_immutable_id: typing.Optional[builtins.str] = None,
        physical_delivery_office_name: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        usage_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::AzureAD::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: The name to display in the address book for the user.
        :param password: The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
        :param user_principal_name: The User Principal Name of the User.
        :param account_enabled: ``true`` if the account should be enabled, otherwise ``false``. Defaults to ``true``. Default: true`.
        :param city: The city in which the user is located.
        :param company_name: The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
        :param country: The country/region in which the user is located; for example, “US” or “UK”.
        :param department: The name for the department in which the user works.
        :param force_password_change: ``true`` if the User is forced to change the password during the next sign-in. Defaults to ``false``. Default: false`.
        :param given_name: The given name (first name) of the user.
        :param immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. Deprecated in favour of ``onpremises_immutable_id``.
        :param job_title: The user’s job title.
        :param mail_nickname: The mail alias for the user. Defaults to the user name part of the User Principal Name. Default: the user name part of the User Principal Name.
        :param mobile: The primary cellular telephone number for the user. Deprecated in favour of ``mobile_phone``.
        :param mobile_phone: The primary cellular telephone number for the user.
        :param office_location: The office location in the user's place of business.
        :param onpremises_immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
        :param physical_delivery_office_name: The office location in the user's place of business. Deprecated in favour of ``office_location``.
        :param postal_code: The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
        :param state: The state or province in the user's address.
        :param street_address: The street address of the user's place of business.
        :param surname: The user's surname (family name or last name).
        :param usage_location: The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set.
        '''
        props = CfnUserProps(
            display_name=display_name,
            password=password,
            user_principal_name=user_principal_name,
            account_enabled=account_enabled,
            city=city,
            company_name=company_name,
            country=country,
            department=department,
            force_password_change=force_password_change,
            given_name=given_name,
            immutable_id=immutable_id,
            job_title=job_title,
            mail_nickname=mail_nickname,
            mobile=mobile,
            mobile_phone=mobile_phone,
            office_location=office_location,
            onpremises_immutable_id=onpremises_immutable_id,
            physical_delivery_office_name=physical_delivery_office_name,
            postal_code=postal_code,
            state=state,
            street_address=street_address,
            surname=surname,
            usage_location=usage_location,
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
        '''Attribute ``TF::AzureAD::User.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMail")
    def attr_mail(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.Mail``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMail"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrObjectId")
    def attr_object_id(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.ObjectId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrObjectId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOnpremisesSamAccountName")
    def attr_onpremises_sam_account_name(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.OnpremisesSamAccountName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOnpremisesSamAccountName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOnpremisesUserPrincipalName")
    def attr_onpremises_user_principal_name(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.OnpremisesUserPrincipalName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOnpremisesUserPrincipalName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserType")
    def attr_user_type(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::User.UserType``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "password": "password",
        "user_principal_name": "userPrincipalName",
        "account_enabled": "accountEnabled",
        "city": "city",
        "company_name": "companyName",
        "country": "country",
        "department": "department",
        "force_password_change": "forcePasswordChange",
        "given_name": "givenName",
        "immutable_id": "immutableId",
        "job_title": "jobTitle",
        "mail_nickname": "mailNickname",
        "mobile": "mobile",
        "mobile_phone": "mobilePhone",
        "office_location": "officeLocation",
        "onpremises_immutable_id": "onpremisesImmutableId",
        "physical_delivery_office_name": "physicalDeliveryOfficeName",
        "postal_code": "postalCode",
        "state": "state",
        "street_address": "streetAddress",
        "surname": "surname",
        "usage_location": "usageLocation",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        password: builtins.str,
        user_principal_name: builtins.str,
        account_enabled: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        force_password_change: typing.Optional[builtins.bool] = None,
        given_name: typing.Optional[builtins.str] = None,
        immutable_id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        mail_nickname: typing.Optional[builtins.str] = None,
        mobile: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office_location: typing.Optional[builtins.str] = None,
        onpremises_immutable_id: typing.Optional[builtins.str] = None,
        physical_delivery_office_name: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        usage_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Manages a User within Azure Active Directory.

        -> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to ``Directory.ReadWrite.All`` within the ``Windows Azure Active Directory`` API.

        :param display_name: The name to display in the address book for the user.
        :param password: The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
        :param user_principal_name: The User Principal Name of the User.
        :param account_enabled: ``true`` if the account should be enabled, otherwise ``false``. Defaults to ``true``. Default: true`.
        :param city: The city in which the user is located.
        :param company_name: The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
        :param country: The country/region in which the user is located; for example, “US” or “UK”.
        :param department: The name for the department in which the user works.
        :param force_password_change: ``true`` if the User is forced to change the password during the next sign-in. Defaults to ``false``. Default: false`.
        :param given_name: The given name (first name) of the user.
        :param immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. Deprecated in favour of ``onpremises_immutable_id``.
        :param job_title: The user’s job title.
        :param mail_nickname: The mail alias for the user. Defaults to the user name part of the User Principal Name. Default: the user name part of the User Principal Name.
        :param mobile: The primary cellular telephone number for the user. Deprecated in favour of ``mobile_phone``.
        :param mobile_phone: The primary cellular telephone number for the user.
        :param office_location: The office location in the user's place of business.
        :param onpremises_immutable_id: The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
        :param physical_delivery_office_name: The office location in the user's place of business. Deprecated in favour of ``office_location``.
        :param postal_code: The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
        :param state: The state or province in the user's address.
        :param street_address: The street address of the user's place of business.
        :param surname: The user's surname (family name or last name).
        :param usage_location: The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set.

        :schema: CfnUserProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "password": password,
            "user_principal_name": user_principal_name,
        }
        if account_enabled is not None:
            self._values["account_enabled"] = account_enabled
        if city is not None:
            self._values["city"] = city
        if company_name is not None:
            self._values["company_name"] = company_name
        if country is not None:
            self._values["country"] = country
        if department is not None:
            self._values["department"] = department
        if force_password_change is not None:
            self._values["force_password_change"] = force_password_change
        if given_name is not None:
            self._values["given_name"] = given_name
        if immutable_id is not None:
            self._values["immutable_id"] = immutable_id
        if job_title is not None:
            self._values["job_title"] = job_title
        if mail_nickname is not None:
            self._values["mail_nickname"] = mail_nickname
        if mobile is not None:
            self._values["mobile"] = mobile
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if office_location is not None:
            self._values["office_location"] = office_location
        if onpremises_immutable_id is not None:
            self._values["onpremises_immutable_id"] = onpremises_immutable_id
        if physical_delivery_office_name is not None:
            self._values["physical_delivery_office_name"] = physical_delivery_office_name
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if state is not None:
            self._values["state"] = state
        if street_address is not None:
            self._values["street_address"] = street_address
        if surname is not None:
            self._values["surname"] = surname
        if usage_location is not None:
            self._values["usage_location"] = usage_location

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name to display in the address book for the user.

        :schema: CfnUserProps#DisplayName
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password for the User.

        The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.

        :schema: CfnUserProps#Password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_principal_name(self) -> builtins.str:
        '''The User Principal Name of the User.

        :schema: CfnUserProps#UserPrincipalName
        '''
        result = self._values.get("user_principal_name")
        assert result is not None, "Required property 'user_principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_enabled(self) -> typing.Optional[builtins.bool]:
        '''``true`` if the account should be enabled, otherwise ``false``.

        Defaults to ``true``.

        :default: true`.

        :schema: CfnUserProps#AccountEnabled
        '''
        result = self._values.get("account_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''The city in which the user is located.

        :schema: CfnUserProps#City
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company_name(self) -> typing.Optional[builtins.str]:
        '''The company name which the user is associated.

        This property can be useful for describing the company that an external user comes from.

        :schema: CfnUserProps#CompanyName
        '''
        result = self._values.get("company_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''The country/region in which the user is located;

        for example, “US” or “UK”.

        :schema: CfnUserProps#Country
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''The name for the department in which the user works.

        :schema: CfnUserProps#Department
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_password_change(self) -> typing.Optional[builtins.bool]:
        '''``true`` if the User is forced to change the password during the next sign-in.

        Defaults to ``false``.

        :default: false`.

        :schema: CfnUserProps#ForcePasswordChange
        '''
        result = self._values.get("force_password_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''The given name (first name) of the user.

        :schema: CfnUserProps#GivenName
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def immutable_id(self) -> typing.Optional[builtins.str]:
        '''The value used to associate an on-premise Active Directory user account with their Azure AD user object.

        Deprecated in favour of ``onpremises_immutable_id``.

        :schema: CfnUserProps#ImmutableId
        '''
        result = self._values.get("immutable_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_title(self) -> typing.Optional[builtins.str]:
        '''The user’s job title.

        :schema: CfnUserProps#JobTitle
        '''
        result = self._values.get("job_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mail_nickname(self) -> typing.Optional[builtins.str]:
        '''The mail alias for the user.

        Defaults to the user name part of the User Principal Name.

        :default: the user name part of the User Principal Name.

        :schema: CfnUserProps#MailNickname
        '''
        result = self._values.get("mail_nickname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile(self) -> typing.Optional[builtins.str]:
        '''The primary cellular telephone number for the user.

        Deprecated in favour of ``mobile_phone``.

        :schema: CfnUserProps#Mobile
        '''
        result = self._values.get("mobile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''The primary cellular telephone number for the user.

        :schema: CfnUserProps#MobilePhone
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office_location(self) -> typing.Optional[builtins.str]:
        '''The office location in the user's place of business.

        :schema: CfnUserProps#OfficeLocation
        '''
        result = self._values.get("office_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def onpremises_immutable_id(self) -> typing.Optional[builtins.str]:
        '''The value used to associate an on-premise Active Directory user account with their Azure AD user object.

        This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.

        :schema: CfnUserProps#OnpremisesImmutableId
        '''
        result = self._values.get("onpremises_immutable_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def physical_delivery_office_name(self) -> typing.Optional[builtins.str]:
        '''The office location in the user's place of business.

        Deprecated in favour of ``office_location``.

        :schema: CfnUserProps#PhysicalDeliveryOfficeName
        '''
        result = self._values.get("physical_delivery_office_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''The postal code for the user's postal address.

        The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.

        :schema: CfnUserProps#PostalCode
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state or province in the user's address.

        :schema: CfnUserProps#State
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''The street address of the user's place of business.

        :schema: CfnUserProps#StreetAddress
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''The user's surname (family name or last name).

        :schema: CfnUserProps#Surname
        '''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usage_location(self) -> typing.Optional[builtins.str]:
        '''The usage location of the User.

        Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: ``NO``, ``JP``, and ``GB``. Cannot be reset to null once set.

        :schema: CfnUserProps#UsageLocation
        '''
        result = self._values.get("usage_location")
        return typing.cast(typing.Optional[builtins.str], result)

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
