'''
# AWS CDK CloudFormation Constructs for TF::Cloudflare::Record

Provides a Cloudflare record resource.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/cloudflare/TF-Cloudflare-Record/docs/README.md)
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


class CfnRecord(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-cloudflare-record.CfnRecord",
):
    '''A CloudFormation ``TF::Cloudflare::Record``.

    :cloudformationResource: TF::Cloudflare::Record
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        data: typing.Optional[typing.Sequence["DataDefinition"]] = None,
        metadata: typing.Optional[typing.Sequence["MetadataDefinition"]] = None,
        priority: typing.Optional[jsii.Number] = None,
        proxiable: typing.Optional[builtins.bool] = None,
        proxied: typing.Optional[builtins.bool] = None,
        timeouts: typing.Optional["TimeoutsDefinition"] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::Cloudflare::Record``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the record.
        :param type: The type of the record.
        :param zone_id: The DNS zone ID to add the record to.
        :param data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or ``value`` must be specified.
        :param metadata: 
        :param priority: The priority of the record.
        :param proxiable: 
        :param proxied: Whether the record gets Cloudflare's origin protection; defaults to ``false``.
        :param timeouts: 
        :param ttl: The TTL of the record (`automatic: '1' <https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record>`_).
        :param value: The (string) value of the record. Either this or ``data`` must be specified.
        '''
        props = CfnRecordProps(
            name=name,
            type=type,
            zone_id=zone_id,
            data=data,
            metadata=metadata,
            priority=priority,
            proxiable=proxiable,
            proxied=proxied,
            timeouts=timeouts,
            ttl=ttl,
            value=value,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedOn")
    def attr_created_on(self) -> builtins.str:
        '''Attribute ``TF::Cloudflare::Record.CreatedOn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedOn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHostname")
    def attr_hostname(self) -> builtins.str:
        '''Attribute ``TF::Cloudflare::Record.Hostname``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostname"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::Cloudflare::Record.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModifiedOn")
    def attr_modified_on(self) -> builtins.str:
        '''Attribute ``TF::Cloudflare::Record.ModifiedOn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedOn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::Cloudflare::Record.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnRecordProps":
        '''Resource props.'''
        return typing.cast("CfnRecordProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-cloudflare-record.CfnRecordProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "zone_id": "zoneId",
        "data": "data",
        "metadata": "metadata",
        "priority": "priority",
        "proxiable": "proxiable",
        "proxied": "proxied",
        "timeouts": "timeouts",
        "ttl": "ttl",
        "value": "value",
    },
)
class CfnRecordProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        data: typing.Optional[typing.Sequence["DataDefinition"]] = None,
        metadata: typing.Optional[typing.Sequence["MetadataDefinition"]] = None,
        priority: typing.Optional[jsii.Number] = None,
        proxiable: typing.Optional[builtins.bool] = None,
        proxied: typing.Optional[builtins.bool] = None,
        timeouts: typing.Optional["TimeoutsDefinition"] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Provides a Cloudflare record resource.

        :param name: The name of the record.
        :param type: The type of the record.
        :param zone_id: The DNS zone ID to add the record to.
        :param data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or ``value`` must be specified.
        :param metadata: 
        :param priority: The priority of the record.
        :param proxiable: 
        :param proxied: Whether the record gets Cloudflare's origin protection; defaults to ``false``.
        :param timeouts: 
        :param ttl: The TTL of the record (`automatic: '1' <https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record>`_).
        :param value: The (string) value of the record. Either this or ``data`` must be specified.

        :schema: CfnRecordProps
        '''
        if isinstance(timeouts, dict):
            timeouts = TimeoutsDefinition(**timeouts)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
            "zone_id": zone_id,
        }
        if data is not None:
            self._values["data"] = data
        if metadata is not None:
            self._values["metadata"] = metadata
        if priority is not None:
            self._values["priority"] = priority
        if proxiable is not None:
            self._values["proxiable"] = proxiable
        if proxied is not None:
            self._values["proxied"] = proxied
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the record.

        :schema: CfnRecordProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the record.

        :schema: CfnRecordProps#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The DNS zone ID to add the record to.

        :schema: CfnRecordProps#ZoneId
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(self) -> typing.Optional[typing.List["DataDefinition"]]:
        '''Map of attributes that constitute the record value.

        Primarily used for LOC and SRV record types. Either this or ``value`` must be specified.

        :schema: CfnRecordProps#Data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.List["DataDefinition"]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List["MetadataDefinition"]]:
        '''
        :schema: CfnRecordProps#Metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List["MetadataDefinition"]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority of the record.

        :schema: CfnRecordProps#Priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proxiable(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnRecordProps#Proxiable
        '''
        result = self._values.get("proxiable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def proxied(self) -> typing.Optional[builtins.bool]:
        '''Whether the record gets Cloudflare's origin protection;

        defaults to ``false``.

        :schema: CfnRecordProps#Proxied
        '''
        result = self._values.get("proxied")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["TimeoutsDefinition"]:
        '''
        :schema: CfnRecordProps#Timeouts
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["TimeoutsDefinition"], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''The TTL of the record (`automatic: '1' <https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record>`_).

        :schema: CfnRecordProps#Ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The (string) value of the record.

        Either this or ``data`` must be specified.

        :schema: CfnRecordProps#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-cloudflare-record.DataDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class DataDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: DataDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: DataDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: DataDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-cloudflare-record.MetadataDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class MetadataDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: MetadataDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: MetadataDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: MetadataDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-cloudflare-record.TimeoutsDefinition",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class TimeoutsDefinition:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: 
        :param update: 

        :schema: TimeoutsDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Update
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeoutsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRecord",
    "CfnRecordProps",
    "DataDefinition",
    "MetadataDefinition",
    "TimeoutsDefinition",
]

publication.publish()
