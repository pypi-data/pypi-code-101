'''
# AWS::Lightsail Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lightsail as lightsail
```
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


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDatabase(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lightsail.CfnDatabase",
):
    '''A CloudFormation ``AWS::Lightsail::Database``.

    :cloudformationResource: AWS::Lightsail::Database
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        relational_database_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDatabase.RelationalDatabaseParameterProperty"]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Database``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param master_database_name: ``AWS::Lightsail::Database.MasterDatabaseName``.
        :param master_username: ``AWS::Lightsail::Database.MasterUsername``.
        :param relational_database_blueprint_id: ``AWS::Lightsail::Database.RelationalDatabaseBlueprintId``.
        :param relational_database_bundle_id: ``AWS::Lightsail::Database.RelationalDatabaseBundleId``.
        :param relational_database_name: ``AWS::Lightsail::Database.RelationalDatabaseName``.
        :param availability_zone: ``AWS::Lightsail::Database.AvailabilityZone``.
        :param backup_retention: ``AWS::Lightsail::Database.BackupRetention``.
        :param ca_certificate_identifier: ``AWS::Lightsail::Database.CaCertificateIdentifier``.
        :param master_user_password: ``AWS::Lightsail::Database.MasterUserPassword``.
        :param preferred_backup_window: ``AWS::Lightsail::Database.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::Lightsail::Database.PreferredMaintenanceWindow``.
        :param publicly_accessible: ``AWS::Lightsail::Database.PubliclyAccessible``.
        :param relational_database_parameters: ``AWS::Lightsail::Database.RelationalDatabaseParameters``.
        :param rotate_master_user_password: ``AWS::Lightsail::Database.RotateMasterUserPassword``.
        :param tags: ``AWS::Lightsail::Database.Tags``.
        '''
        props = CfnDatabaseProps(
            master_database_name=master_database_name,
            master_username=master_username,
            relational_database_blueprint_id=relational_database_blueprint_id,
            relational_database_bundle_id=relational_database_bundle_id,
            relational_database_name=relational_database_name,
            availability_zone=availability_zone,
            backup_retention=backup_retention,
            ca_certificate_identifier=ca_certificate_identifier,
            master_user_password=master_user_password,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            relational_database_parameters=relational_database_parameters,
            rotate_master_user_password=rotate_master_user_password,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDatabaseArn")
    def attr_database_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DatabaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatabaseArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Lightsail::Database.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterDatabaseName")
    def master_database_name(self) -> builtins.str:
        '''``AWS::Lightsail::Database.MasterDatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterDatabaseName"))

    @master_database_name.setter
    def master_database_name(self, value: builtins.str) -> None:
        jsii.set(self, "masterDatabaseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        '''``AWS::Lightsail::Database.MasterUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        jsii.set(self, "masterUsername", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseBlueprintId")
    def relational_database_blueprint_id(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseBlueprintId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBlueprintId"))

    @relational_database_blueprint_id.setter
    def relational_database_blueprint_id(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseBlueprintId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseBundleId")
    def relational_database_bundle_id(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseBundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBundleId"))

    @relational_database_bundle_id.setter
    def relational_database_bundle_id(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseBundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseName")
    def relational_database_name(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseName"))

    @relational_database_name.setter
    def relational_database_name(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="backupRetention")
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.BackupRetention``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "backupRetention"))

    @backup_retention.setter
    def backup_retention(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "backupRetention", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.CaCertificateIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificateIdentifier"))

    @ca_certificate_identifier.setter
    def ca_certificate_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "caCertificateIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.MasterUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "masterUserPassword", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.PreferredBackupWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.PubliclyAccessible``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseParameters")
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatabase.RelationalDatabaseParameterProperty"]]]]:
        '''``AWS::Lightsail::Database.RelationalDatabaseParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatabase.RelationalDatabaseParameterProperty"]]]], jsii.get(self, "relationalDatabaseParameters"))

    @relational_database_parameters.setter
    def relational_database_parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatabase.RelationalDatabaseParameterProperty"]]]],
    ) -> None:
        jsii.set(self, "relationalDatabaseParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotateMasterUserPassword")
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.RotateMasterUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "rotateMasterUserPassword"))

    @rotate_master_user_password.setter
    def rotate_master_user_password(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "rotateMasterUserPassword", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnDatabase.RelationalDatabaseParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_values": "allowedValues",
            "apply_method": "applyMethod",
            "apply_type": "applyType",
            "data_type": "dataType",
            "description": "description",
            "is_modifiable": "isModifiable",
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class RelationalDatabaseParameterProperty:
        def __init__(
            self,
            *,
            allowed_values: typing.Optional[builtins.str] = None,
            apply_method: typing.Optional[builtins.str] = None,
            apply_type: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            is_modifiable: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            parameter_name: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param allowed_values: ``CfnDatabase.RelationalDatabaseParameterProperty.AllowedValues``.
            :param apply_method: ``CfnDatabase.RelationalDatabaseParameterProperty.ApplyMethod``.
            :param apply_type: ``CfnDatabase.RelationalDatabaseParameterProperty.ApplyType``.
            :param data_type: ``CfnDatabase.RelationalDatabaseParameterProperty.DataType``.
            :param description: ``CfnDatabase.RelationalDatabaseParameterProperty.Description``.
            :param is_modifiable: ``CfnDatabase.RelationalDatabaseParameterProperty.IsModifiable``.
            :param parameter_name: ``CfnDatabase.RelationalDatabaseParameterProperty.ParameterName``.
            :param parameter_value: ``CfnDatabase.RelationalDatabaseParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if apply_method is not None:
                self._values["apply_method"] = apply_method
            if apply_type is not None:
                self._values["apply_type"] = apply_type
            if data_type is not None:
                self._values["data_type"] = data_type
            if description is not None:
                self._values["description"] = description
            if is_modifiable is not None:
                self._values["is_modifiable"] = is_modifiable
            if parameter_name is not None:
                self._values["parameter_name"] = parameter_name
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def allowed_values(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_method(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.ApplyMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod
            '''
            result = self._values.get("apply_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.ApplyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype
            '''
            result = self._values.get("apply_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_modifiable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.IsModifiable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable
            '''
            result = self._values.get("is_modifiable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def parameter_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.ParameterName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername
            '''
            result = self._values.get("parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDatabase.RelationalDatabaseParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lightsail.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "master_database_name": "masterDatabaseName",
        "master_username": "masterUsername",
        "relational_database_blueprint_id": "relationalDatabaseBlueprintId",
        "relational_database_bundle_id": "relationalDatabaseBundleId",
        "relational_database_name": "relationalDatabaseName",
        "availability_zone": "availabilityZone",
        "backup_retention": "backupRetention",
        "ca_certificate_identifier": "caCertificateIdentifier",
        "master_user_password": "masterUserPassword",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "relational_database_parameters": "relationalDatabaseParameters",
        "rotate_master_user_password": "rotateMasterUserPassword",
        "tags": "tags",
    },
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        relational_database_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDatabase.RelationalDatabaseParameterProperty]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Lightsail::Database``.

        :param master_database_name: ``AWS::Lightsail::Database.MasterDatabaseName``.
        :param master_username: ``AWS::Lightsail::Database.MasterUsername``.
        :param relational_database_blueprint_id: ``AWS::Lightsail::Database.RelationalDatabaseBlueprintId``.
        :param relational_database_bundle_id: ``AWS::Lightsail::Database.RelationalDatabaseBundleId``.
        :param relational_database_name: ``AWS::Lightsail::Database.RelationalDatabaseName``.
        :param availability_zone: ``AWS::Lightsail::Database.AvailabilityZone``.
        :param backup_retention: ``AWS::Lightsail::Database.BackupRetention``.
        :param ca_certificate_identifier: ``AWS::Lightsail::Database.CaCertificateIdentifier``.
        :param master_user_password: ``AWS::Lightsail::Database.MasterUserPassword``.
        :param preferred_backup_window: ``AWS::Lightsail::Database.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::Lightsail::Database.PreferredMaintenanceWindow``.
        :param publicly_accessible: ``AWS::Lightsail::Database.PubliclyAccessible``.
        :param relational_database_parameters: ``AWS::Lightsail::Database.RelationalDatabaseParameters``.
        :param rotate_master_user_password: ``AWS::Lightsail::Database.RotateMasterUserPassword``.
        :param tags: ``AWS::Lightsail::Database.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "master_database_name": master_database_name,
            "master_username": master_username,
            "relational_database_blueprint_id": relational_database_blueprint_id,
            "relational_database_bundle_id": relational_database_bundle_id,
            "relational_database_name": relational_database_name,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if backup_retention is not None:
            self._values["backup_retention"] = backup_retention
        if ca_certificate_identifier is not None:
            self._values["ca_certificate_identifier"] = ca_certificate_identifier
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if relational_database_parameters is not None:
            self._values["relational_database_parameters"] = relational_database_parameters
        if rotate_master_user_password is not None:
            self._values["rotate_master_user_password"] = rotate_master_user_password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def master_database_name(self) -> builtins.str:
        '''``AWS::Lightsail::Database.MasterDatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
        '''
        result = self._values.get("master_database_name")
        assert result is not None, "Required property 'master_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_username(self) -> builtins.str:
        '''``AWS::Lightsail::Database.MasterUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
        '''
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_blueprint_id(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseBlueprintId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
        '''
        result = self._values.get("relational_database_blueprint_id")
        assert result is not None, "Required property 'relational_database_blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_bundle_id(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseBundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
        '''
        result = self._values.get("relational_database_bundle_id")
        assert result is not None, "Required property 'relational_database_bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_name(self) -> builtins.str:
        '''``AWS::Lightsail::Database.RelationalDatabaseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
        '''
        result = self._values.get("relational_database_name")
        assert result is not None, "Required property 'relational_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.BackupRetention``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
        '''
        result = self._values.get("backup_retention")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.CaCertificateIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
        '''
        result = self._values.get("ca_certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.MasterUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.PreferredBackupWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Database.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.PubliclyAccessible``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDatabase.RelationalDatabaseParameterProperty]]]]:
        '''``AWS::Lightsail::Database.RelationalDatabaseParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
        '''
        result = self._values.get("relational_database_parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDatabase.RelationalDatabaseParameterProperty]]]], result)

    @builtins.property
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Lightsail::Database.RotateMasterUserPassword``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
        '''
        result = self._values.get("rotate_master_user_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Lightsail::Database.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDisk(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lightsail.CfnDisk",
):
    '''A CloudFormation ``AWS::Lightsail::Disk``.

    :cloudformationResource: AWS::Lightsail::Disk
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnDisk.AddOnProperty", aws_cdk.core.IResolvable]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Disk``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param disk_name: ``AWS::Lightsail::Disk.DiskName``.
        :param size_in_gb: ``AWS::Lightsail::Disk.SizeInGb``.
        :param add_ons: ``AWS::Lightsail::Disk.AddOns``.
        :param availability_zone: ``AWS::Lightsail::Disk.AvailabilityZone``.
        :param tags: ``AWS::Lightsail::Disk.Tags``.
        '''
        props = CfnDiskProps(
            disk_name=disk_name,
            size_in_gb=size_in_gb,
            add_ons=add_ons,
            availability_zone=availability_zone,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachedTo")
    def attr_attached_to(self) -> builtins.str:
        '''
        :cloudformationAttribute: AttachedTo
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachedTo"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentState")
    def attr_attachment_state(self) -> builtins.str:
        '''
        :cloudformationAttribute: AttachmentState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDiskArn")
    def attr_disk_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DiskArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiskArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIops")
    def attr_iops(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Iops
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrIops"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrIsAttached"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPath")
    def attr_path(self) -> builtins.str:
        '''
        :cloudformationAttribute: Path
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''
        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''
        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Lightsail::Disk.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        '''``AWS::Lightsail::Disk.DiskName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
        '''
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        jsii.set(self, "diskName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        '''``AWS::Lightsail::Disk.SizeInGb``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
        '''
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        jsii.set(self, "sizeInGb", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDisk.AddOnProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::Lightsail::Disk.AddOns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDisk.AddOnProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDisk.AddOnProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "addOns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Disk.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnDisk.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDisk.AutoSnapshotAddOnProperty"]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_on_type: ``CfnDisk.AddOnProperty.AddOnType``.
            :param auto_snapshot_add_on_request: ``CfnDisk.AddOnProperty.AutoSnapshotAddOnRequest``.
            :param status: ``CfnDisk.AddOnProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''``CfnDisk.AddOnProperty.AddOnType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDisk.AutoSnapshotAddOnProperty"]]:
            '''``CfnDisk.AddOnProperty.AutoSnapshotAddOnRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDisk.AutoSnapshotAddOnProperty"]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''``CfnDisk.AddOnProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnDisk.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param snapshot_time_of_day: ``CfnDisk.AutoSnapshotAddOnProperty.SnapshotTimeOfDay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''``CfnDisk.AutoSnapshotAddOnProperty.SnapshotTimeOfDay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lightsail.CfnDiskProps",
    jsii_struct_bases=[],
    name_mapping={
        "disk_name": "diskName",
        "size_in_gb": "sizeInGb",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "tags": "tags",
    },
)
class CfnDiskProps:
    def __init__(
        self,
        *,
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnDisk.AddOnProperty, aws_cdk.core.IResolvable]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Lightsail::Disk``.

        :param disk_name: ``AWS::Lightsail::Disk.DiskName``.
        :param size_in_gb: ``AWS::Lightsail::Disk.SizeInGb``.
        :param add_ons: ``AWS::Lightsail::Disk.AddOns``.
        :param availability_zone: ``AWS::Lightsail::Disk.AvailabilityZone``.
        :param tags: ``AWS::Lightsail::Disk.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "disk_name": disk_name,
            "size_in_gb": size_in_gb,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''``AWS::Lightsail::Disk.DiskName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''``AWS::Lightsail::Disk.SizeInGb``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
        '''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDisk.AddOnProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Lightsail::Disk.AddOns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDisk.AddOnProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Disk.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Lightsail::Disk.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDiskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lightsail.CfnInstance",
):
    '''A CloudFormation ``AWS::Lightsail::Instance``.

    :cloudformationResource: AWS::Lightsail::Instance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AddOnProperty"]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.HardwareProperty"]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LocationProperty"]] = None,
        networking: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkingProperty"]] = None,
        state: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.StateProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Instance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param blueprint_id: ``AWS::Lightsail::Instance.BlueprintId``.
        :param bundle_id: ``AWS::Lightsail::Instance.BundleId``.
        :param instance_name: ``AWS::Lightsail::Instance.InstanceName``.
        :param add_ons: ``AWS::Lightsail::Instance.AddOns``.
        :param availability_zone: ``AWS::Lightsail::Instance.AvailabilityZone``.
        :param hardware: ``AWS::Lightsail::Instance.Hardware``.
        :param key_pair_name: ``AWS::Lightsail::Instance.KeyPairName``.
        :param location: ``AWS::Lightsail::Instance.Location``.
        :param networking: ``AWS::Lightsail::Instance.Networking``.
        :param state: ``AWS::Lightsail::Instance.State``.
        :param tags: ``AWS::Lightsail::Instance.Tags``.
        :param user_data: ``AWS::Lightsail::Instance.UserData``.
        '''
        props = CfnInstanceProps(
            blueprint_id=blueprint_id,
            bundle_id=bundle_id,
            instance_name=instance_name,
            add_ons=add_ons,
            availability_zone=availability_zone,
            hardware=hardware,
            key_pair_name=key_pair_name,
            location=location,
            networking=networking,
            state=state,
            tags=tags,
            user_data=user_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHardwareCpuCount")
    def attr_hardware_cpu_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Hardware.CpuCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareCpuCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHardwareRamSizeInGb")
    def attr_hardware_ram_size_in_gb(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Hardware.RamSizeInGb
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareRamSizeInGb"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrInstanceArn")
    def attr_instance_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: InstanceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsStaticIp")
    def attr_is_static_ip(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: IsStaticIp
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrIsStaticIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationAvailabilityZone")
    def attr_location_availability_zone(self) -> builtins.str:
        '''
        :cloudformationAttribute: Location.AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationAvailabilityZone"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationRegionName")
    def attr_location_region_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Location.RegionName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationRegionName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNetworkingMonthlyTransferGbPerMonthAllocated")
    def attr_networking_monthly_transfer_gb_per_month_allocated(self) -> builtins.str:
        '''
        :cloudformationAttribute: Networking.MonthlyTransfer.GbPerMonthAllocated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkingMonthlyTransferGbPerMonthAllocated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrivateIpAddress")
    def attr_private_ip_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrivateIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicIpAddress")
    def attr_public_ip_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublicIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSshKeyName")
    def attr_ssh_key_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: SshKeyName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshKeyName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStateCode")
    def attr_state_code(self) -> jsii.Number:
        '''
        :cloudformationAttribute: State.Code
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrStateCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: State.Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''
        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Lightsail::Instance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blueprintId")
    def blueprint_id(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.BlueprintId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
        '''
        return typing.cast(builtins.str, jsii.get(self, "blueprintId"))

    @blueprint_id.setter
    def blueprint_id(self, value: builtins.str) -> None:
        jsii.set(self, "blueprintId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceName")
    def instance_name(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.InstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceName"))

    @instance_name.setter
    def instance_name(self, value: builtins.str) -> None:
        jsii.set(self, "instanceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AddOnProperty"]]]]:
        '''``AWS::Lightsail::Instance.AddOns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AddOnProperty"]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AddOnProperty"]]]],
    ) -> None:
        jsii.set(self, "addOns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hardware")
    def hardware(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.HardwareProperty"]]:
        '''``AWS::Lightsail::Instance.Hardware``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.HardwareProperty"]], jsii.get(self, "hardware"))

    @hardware.setter
    def hardware(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.HardwareProperty"]],
    ) -> None:
        jsii.set(self, "hardware", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyPairName")
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.KeyPairName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPairName"))

    @key_pair_name.setter
    def key_pair_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "keyPairName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LocationProperty"]]:
        '''``AWS::Lightsail::Instance.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-location
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LocationProperty"]],
    ) -> None:
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networking")
    def networking(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkingProperty"]]:
        '''``AWS::Lightsail::Instance.Networking``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkingProperty"]], jsii.get(self, "networking"))

    @networking.setter
    def networking(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkingProperty"]],
    ) -> None:
        jsii.set(self, "networking", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.StateProperty"]]:
        '''``AWS::Lightsail::Instance.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-state
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.StateProperty"]], jsii.get(self, "state"))

    @state.setter
    def state(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.StateProperty"]],
    ) -> None:
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.UserData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "userData", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AutoSnapshotAddOnProperty"]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_on_type: ``CfnInstance.AddOnProperty.AddOnType``.
            :param auto_snapshot_add_on_request: ``CfnInstance.AddOnProperty.AutoSnapshotAddOnRequest``.
            :param status: ``CfnInstance.AddOnProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''``CfnInstance.AddOnProperty.AddOnType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AutoSnapshotAddOnProperty"]]:
            '''``CfnInstance.AddOnProperty.AutoSnapshotAddOnRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AutoSnapshotAddOnProperty"]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.AddOnProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param snapshot_time_of_day: ``CfnInstance.AutoSnapshotAddOnProperty.SnapshotTimeOfDay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.AutoSnapshotAddOnProperty.SnapshotTimeOfDay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.DiskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "disk_name": "diskName",
            "path": "path",
            "attached_to": "attachedTo",
            "attachment_state": "attachmentState",
            "iops": "iops",
            "is_system_disk": "isSystemDisk",
            "size_in_gb": "sizeInGb",
        },
    )
    class DiskProperty:
        def __init__(
            self,
            *,
            disk_name: builtins.str,
            path: builtins.str,
            attached_to: typing.Optional[builtins.str] = None,
            attachment_state: typing.Optional[builtins.str] = None,
            iops: typing.Optional[jsii.Number] = None,
            is_system_disk: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            size_in_gb: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param disk_name: ``CfnInstance.DiskProperty.DiskName``.
            :param path: ``CfnInstance.DiskProperty.Path``.
            :param attached_to: ``CfnInstance.DiskProperty.AttachedTo``.
            :param attachment_state: ``CfnInstance.DiskProperty.AttachmentState``.
            :param iops: ``CfnInstance.DiskProperty.IOPS``.
            :param is_system_disk: ``CfnInstance.DiskProperty.IsSystemDisk``.
            :param size_in_gb: ``CfnInstance.DiskProperty.SizeInGb``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "disk_name": disk_name,
                "path": path,
            }
            if attached_to is not None:
                self._values["attached_to"] = attached_to
            if attachment_state is not None:
                self._values["attachment_state"] = attachment_state
            if iops is not None:
                self._values["iops"] = iops
            if is_system_disk is not None:
                self._values["is_system_disk"] = is_system_disk
            if size_in_gb is not None:
                self._values["size_in_gb"] = size_in_gb

        @builtins.property
        def disk_name(self) -> builtins.str:
            '''``CfnInstance.DiskProperty.DiskName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname
            '''
            result = self._values.get("disk_name")
            assert result is not None, "Required property 'disk_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''``CfnInstance.DiskProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attached_to(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.DiskProperty.AttachedTo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto
            '''
            result = self._values.get("attached_to")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def attachment_state(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.DiskProperty.AttachmentState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate
            '''
            result = self._values.get("attachment_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.DiskProperty.IOPS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def is_system_disk(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnInstance.DiskProperty.IsSystemDisk``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk
            '''
            result = self._values.get("is_system_disk")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def size_in_gb(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.DiskProperty.SizeInGb``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb
            '''
            result = self._values.get("size_in_gb")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DiskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.HardwareProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_count": "cpuCount",
            "disks": "disks",
            "ram_size_in_gb": "ramSizeInGb",
        },
    )
    class HardwareProperty:
        def __init__(
            self,
            *,
            cpu_count: typing.Optional[jsii.Number] = None,
            disks: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.DiskProperty"]]]] = None,
            ram_size_in_gb: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param cpu_count: ``CfnInstance.HardwareProperty.CpuCount``.
            :param disks: ``CfnInstance.HardwareProperty.Disks``.
            :param ram_size_in_gb: ``CfnInstance.HardwareProperty.RamSizeInGb``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu_count is not None:
                self._values["cpu_count"] = cpu_count
            if disks is not None:
                self._values["disks"] = disks
            if ram_size_in_gb is not None:
                self._values["ram_size_in_gb"] = ram_size_in_gb

        @builtins.property
        def cpu_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.HardwareProperty.CpuCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount
            '''
            result = self._values.get("cpu_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def disks(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.DiskProperty"]]]]:
            '''``CfnInstance.HardwareProperty.Disks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks
            '''
            result = self._values.get("disks")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.DiskProperty"]]]], result)

        @builtins.property
        def ram_size_in_gb(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.HardwareProperty.RamSizeInGb``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb
            '''
            result = self._values.get("ram_size_in_gb")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HardwareProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "region_name": "regionName",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param availability_zone: ``CfnInstance.LocationProperty.AvailabilityZone``.
            :param region_name: ``CfnInstance.LocationProperty.RegionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.LocationProperty.AvailabilityZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.LocationProperty.RegionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.MonthlyTransferProperty",
        jsii_struct_bases=[],
        name_mapping={"gb_per_month_allocated": "gbPerMonthAllocated"},
    )
    class MonthlyTransferProperty:
        def __init__(
            self,
            *,
            gb_per_month_allocated: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param gb_per_month_allocated: ``CfnInstance.MonthlyTransferProperty.GbPerMonthAllocated``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if gb_per_month_allocated is not None:
                self._values["gb_per_month_allocated"] = gb_per_month_allocated

        @builtins.property
        def gb_per_month_allocated(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.MonthlyTransferProperty.GbPerMonthAllocated``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated
            '''
            result = self._values.get("gb_per_month_allocated")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlyTransferProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.NetworkingProperty",
        jsii_struct_bases=[],
        name_mapping={"ports": "ports", "monthly_transfer": "monthlyTransfer"},
    )
    class NetworkingProperty:
        def __init__(
            self,
            *,
            ports: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.PortProperty"]]],
            monthly_transfer: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param ports: ``CfnInstance.NetworkingProperty.Ports``.
            :param monthly_transfer: ``CfnInstance.NetworkingProperty.MonthlyTransfer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ports": ports,
            }
            if monthly_transfer is not None:
                self._values["monthly_transfer"] = monthly_transfer

        @builtins.property
        def ports(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.PortProperty"]]]:
            '''``CfnInstance.NetworkingProperty.Ports``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports
            '''
            result = self._values.get("ports")
            assert result is not None, "Required property 'ports' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.PortProperty"]]], result)

        @builtins.property
        def monthly_transfer(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.NetworkingProperty.MonthlyTransfer``.'''
            result = self._values.get("monthly_transfer")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.PortProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_direction": "accessDirection",
            "access_from": "accessFrom",
            "access_type": "accessType",
            "cidr_list_aliases": "cidrListAliases",
            "cidrs": "cidrs",
            "common_name": "commonName",
            "from_port": "fromPort",
            "ipv6_cidrs": "ipv6Cidrs",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class PortProperty:
        def __init__(
            self,
            *,
            access_direction: typing.Optional[builtins.str] = None,
            access_from: typing.Optional[builtins.str] = None,
            access_type: typing.Optional[builtins.str] = None,
            cidr_list_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
            cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            common_name: typing.Optional[builtins.str] = None,
            from_port: typing.Optional[jsii.Number] = None,
            ipv6_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            protocol: typing.Optional[builtins.str] = None,
            to_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param access_direction: ``CfnInstance.PortProperty.AccessDirection``.
            :param access_from: ``CfnInstance.PortProperty.AccessFrom``.
            :param access_type: ``CfnInstance.PortProperty.AccessType``.
            :param cidr_list_aliases: ``CfnInstance.PortProperty.CidrListAliases``.
            :param cidrs: ``CfnInstance.PortProperty.Cidrs``.
            :param common_name: ``CfnInstance.PortProperty.CommonName``.
            :param from_port: ``CfnInstance.PortProperty.FromPort``.
            :param ipv6_cidrs: ``CfnInstance.PortProperty.Ipv6Cidrs``.
            :param protocol: ``CfnInstance.PortProperty.Protocol``.
            :param to_port: ``CfnInstance.PortProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_direction is not None:
                self._values["access_direction"] = access_direction
            if access_from is not None:
                self._values["access_from"] = access_from
            if access_type is not None:
                self._values["access_type"] = access_type
            if cidr_list_aliases is not None:
                self._values["cidr_list_aliases"] = cidr_list_aliases
            if cidrs is not None:
                self._values["cidrs"] = cidrs
            if common_name is not None:
                self._values["common_name"] = common_name
            if from_port is not None:
                self._values["from_port"] = from_port
            if ipv6_cidrs is not None:
                self._values["ipv6_cidrs"] = ipv6_cidrs
            if protocol is not None:
                self._values["protocol"] = protocol
            if to_port is not None:
                self._values["to_port"] = to_port

        @builtins.property
        def access_direction(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.PortProperty.AccessDirection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection
            '''
            result = self._values.get("access_direction")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_from(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.PortProperty.AccessFrom``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom
            '''
            result = self._values.get("access_from")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_type(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.PortProperty.AccessType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype
            '''
            result = self._values.get("access_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cidr_list_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnInstance.PortProperty.CidrListAliases``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases
            '''
            result = self._values.get("cidr_list_aliases")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnInstance.PortProperty.Cidrs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs
            '''
            result = self._values.get("cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.PortProperty.CommonName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def from_port(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.PortProperty.FromPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport
            '''
            result = self._values.get("from_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ipv6_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnInstance.PortProperty.Ipv6Cidrs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs
            '''
            result = self._values.get("ipv6_cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.PortProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def to_port(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.PortProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport
            '''
            result = self._values.get("to_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lightsail.CfnInstance.StateProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "name": "name"},
    )
    class StateProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param code: ``CfnInstance.StateProperty.Code``.
            :param name: ``CfnInstance.StateProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def code(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.StateProperty.Code``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.StateProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lightsail.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "blueprint_id": "blueprintId",
        "bundle_id": "bundleId",
        "instance_name": "instanceName",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "hardware": "hardware",
        "key_pair_name": "keyPairName",
        "location": "location",
        "networking": "networking",
        "state": "state",
        "tags": "tags",
        "user_data": "userData",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInstance.AddOnProperty]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.HardwareProperty]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.LocationProperty]] = None,
        networking: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.NetworkingProperty]] = None,
        state: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.StateProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Lightsail::Instance``.

        :param blueprint_id: ``AWS::Lightsail::Instance.BlueprintId``.
        :param bundle_id: ``AWS::Lightsail::Instance.BundleId``.
        :param instance_name: ``AWS::Lightsail::Instance.InstanceName``.
        :param add_ons: ``AWS::Lightsail::Instance.AddOns``.
        :param availability_zone: ``AWS::Lightsail::Instance.AvailabilityZone``.
        :param hardware: ``AWS::Lightsail::Instance.Hardware``.
        :param key_pair_name: ``AWS::Lightsail::Instance.KeyPairName``.
        :param location: ``AWS::Lightsail::Instance.Location``.
        :param networking: ``AWS::Lightsail::Instance.Networking``.
        :param state: ``AWS::Lightsail::Instance.State``.
        :param tags: ``AWS::Lightsail::Instance.Tags``.
        :param user_data: ``AWS::Lightsail::Instance.UserData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "blueprint_id": blueprint_id,
            "bundle_id": bundle_id,
            "instance_name": instance_name,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if hardware is not None:
            self._values["hardware"] = hardware
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if location is not None:
            self._values["location"] = location
        if networking is not None:
            self._values["networking"] = networking
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def blueprint_id(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.BlueprintId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
        '''
        result = self._values.get("blueprint_id")
        assert result is not None, "Required property 'blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_name(self) -> builtins.str:
        '''``AWS::Lightsail::Instance.InstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
        '''
        result = self._values.get("instance_name")
        assert result is not None, "Required property 'instance_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstance.AddOnProperty]]]]:
        '''``AWS::Lightsail::Instance.AddOns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstance.AddOnProperty]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.HardwareProperty]]:
        '''``AWS::Lightsail::Instance.Hardware``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
        '''
        result = self._values.get("hardware")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.HardwareProperty]], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.KeyPairName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.LocationProperty]]:
        '''``AWS::Lightsail::Instance.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.LocationProperty]], result)

    @builtins.property
    def networking(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.NetworkingProperty]]:
        '''``AWS::Lightsail::Instance.Networking``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
        '''
        result = self._values.get("networking")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.NetworkingProperty]], result)

    @builtins.property
    def state(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.StateProperty]]:
        '''``AWS::Lightsail::Instance.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.StateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Lightsail::Instance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::Instance.UserData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStaticIp(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lightsail.CfnStaticIp",
):
    '''A CloudFormation ``AWS::Lightsail::StaticIp``.

    :cloudformationResource: AWS::Lightsail::StaticIp
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::StaticIp``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param static_ip_name: ``AWS::Lightsail::StaticIp.StaticIpName``.
        :param attached_to: ``AWS::Lightsail::StaticIp.AttachedTo``.
        '''
        props = CfnStaticIpProps(
            static_ip_name=static_ip_name, attached_to=attached_to
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrIsAttached"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStaticIpArn")
    def attr_static_ip_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: StaticIpArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStaticIpArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="staticIpName")
    def static_ip_name(self) -> builtins.str:
        '''``AWS::Lightsail::StaticIp.StaticIpName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
        '''
        return typing.cast(builtins.str, jsii.get(self, "staticIpName"))

    @static_ip_name.setter
    def static_ip_name(self, value: builtins.str) -> None:
        jsii.set(self, "staticIpName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attachedTo")
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::StaticIp.AttachedTo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachedTo"))

    @attached_to.setter
    def attached_to(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "attachedTo", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lightsail.CfnStaticIpProps",
    jsii_struct_bases=[],
    name_mapping={"static_ip_name": "staticIpName", "attached_to": "attachedTo"},
)
class CfnStaticIpProps:
    def __init__(
        self,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Lightsail::StaticIp``.

        :param static_ip_name: ``AWS::Lightsail::StaticIp.StaticIpName``.
        :param attached_to: ``AWS::Lightsail::StaticIp.AttachedTo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "static_ip_name": static_ip_name,
        }
        if attached_to is not None:
            self._values["attached_to"] = attached_to

    @builtins.property
    def static_ip_name(self) -> builtins.str:
        '''``AWS::Lightsail::StaticIp.StaticIpName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
        '''
        result = self._values.get("static_ip_name")
        assert result is not None, "Required property 'static_ip_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''``AWS::Lightsail::StaticIp.AttachedTo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
        '''
        result = self._values.get("attached_to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStaticIpProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnDisk",
    "CfnDiskProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnStaticIp",
    "CfnStaticIpProps",
]

publication.publish()
