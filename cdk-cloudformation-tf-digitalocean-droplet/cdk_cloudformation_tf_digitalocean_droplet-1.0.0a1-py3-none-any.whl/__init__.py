'''
# AWS CDK CloudFormation Constructs for TF::DigitalOcean::Droplet

Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](https://www.terraform.io/docs/language/resources/provisioners/syntax.html).

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/digitalocean/TF-DigitalOcean-Droplet/docs/README.md)
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


class CfnDroplet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-digitalocean-droplet.CfnDroplet",
):
    '''A CloudFormation ``TF::DigitalOcean::Droplet``.

    :cloudformationResource: TF::DigitalOcean::Droplet
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        region: builtins.str,
        size: builtins.str,
        backups: typing.Optional[builtins.bool] = None,
        ipv6: typing.Optional[builtins.bool] = None,
        locked: typing.Optional[builtins.bool] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        private_networking: typing.Optional[builtins.bool] = None,
        resize_disk: typing.Optional[builtins.bool] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::DigitalOcean::Droplet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param image: The Droplet image ID or slug.
        :param name: The Droplet name.
        :param region: The region to start in.
        :param size: The unique slug that indentifies the type of Droplet. You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.
        :param backups: Boolean controlling if backups are made. Defaults to false. Default: false.
        :param ipv6: Boolean controlling if IPv6 is enabled. Defaults to false. Default: false.
        :param locked: 
        :param monitoring: Boolean controlling whether monitoring agent is installed. Defaults to false. Default: false.
        :param private_networking: Boolean controlling if private networking is enabled. When VPC is enabled on an account, this will provision the Droplet inside of your account's default VPC for the region. Use the ``vpc_uuid`` attribute to specify a different VPC.
        :param resize_disk: Boolean controlling whether to increase the disk size when resizing a Droplet. It defaults to ``true``. When set to ``false``, only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk size is a permanent change**. Increasing only RAM and CPU is reversible.
        :param ssh_keys: A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``. To retrieve this info, use the `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_ or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not be added or removed via this provider. Modifying this field will prompt you to destroy and recreate the Droplet.
        :param tags: A list of the tags to be applied to this Droplet.
        :param user_data: 
        :param volume_ids: 
        :param vpc_uuid: The ID of the VPC where the Droplet will be located.
        '''
        props = CfnDropletProps(
            image=image,
            name=name,
            region=region,
            size=size,
            backups=backups,
            ipv6=ipv6,
            locked=locked,
            monitoring=monitoring,
            private_networking=private_networking,
            resize_disk=resize_disk,
            ssh_keys=ssh_keys,
            tags=tags,
            user_data=user_data,
            volume_ids=volume_ids,
            vpc_uuid=vpc_uuid,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.CreatedAt``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDisk")
    def attr_disk(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Disk``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDisk"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpv4Address")
    def attr_ipv4_address(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv4Address``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv4Address"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpv4AddressPrivate")
    def attr_ipv4_address_private(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv4AddressPrivate``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv4AddressPrivate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpv6Address")
    def attr_ipv6_address(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv6Address``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv6Address"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMemory")
    def attr_memory(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Memory``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMemory"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPriceHourly")
    def attr_price_hourly(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.PriceHourly``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPriceHourly"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPriceMonthly")
    def attr_price_monthly(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.PriceMonthly``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPriceMonthly"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Status``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUrn")
    def attr_urn(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Urn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVcpus")
    def attr_vcpus(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Vcpus``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVcpus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDropletProps":
        '''Resource props.'''
        return typing.cast("CfnDropletProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-digitalocean-droplet.CfnDropletProps",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "name": "name",
        "region": "region",
        "size": "size",
        "backups": "backups",
        "ipv6": "ipv6",
        "locked": "locked",
        "monitoring": "monitoring",
        "private_networking": "privateNetworking",
        "resize_disk": "resizeDisk",
        "ssh_keys": "sshKeys",
        "tags": "tags",
        "user_data": "userData",
        "volume_ids": "volumeIds",
        "vpc_uuid": "vpcUuid",
    },
)
class CfnDropletProps:
    def __init__(
        self,
        *,
        image: builtins.str,
        name: builtins.str,
        region: builtins.str,
        size: builtins.str,
        backups: typing.Optional[builtins.bool] = None,
        ipv6: typing.Optional[builtins.bool] = None,
        locked: typing.Optional[builtins.bool] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        private_networking: typing.Optional[builtins.bool] = None,
        resize_disk: typing.Optional[builtins.bool] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Provides a DigitalOcean Droplet resource.

        This can be used to create,
        modify, and delete Droplets. Droplets also support
        `provisioning <https://www.terraform.io/docs/language/resources/provisioners/syntax.html>`_.

        :param image: The Droplet image ID or slug.
        :param name: The Droplet name.
        :param region: The region to start in.
        :param size: The unique slug that indentifies the type of Droplet. You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.
        :param backups: Boolean controlling if backups are made. Defaults to false. Default: false.
        :param ipv6: Boolean controlling if IPv6 is enabled. Defaults to false. Default: false.
        :param locked: 
        :param monitoring: Boolean controlling whether monitoring agent is installed. Defaults to false. Default: false.
        :param private_networking: Boolean controlling if private networking is enabled. When VPC is enabled on an account, this will provision the Droplet inside of your account's default VPC for the region. Use the ``vpc_uuid`` attribute to specify a different VPC.
        :param resize_disk: Boolean controlling whether to increase the disk size when resizing a Droplet. It defaults to ``true``. When set to ``false``, only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk size is a permanent change**. Increasing only RAM and CPU is reversible.
        :param ssh_keys: A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``. To retrieve this info, use the `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_ or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not be added or removed via this provider. Modifying this field will prompt you to destroy and recreate the Droplet.
        :param tags: A list of the tags to be applied to this Droplet.
        :param user_data: 
        :param volume_ids: 
        :param vpc_uuid: The ID of the VPC where the Droplet will be located.

        :schema: CfnDropletProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
            "name": name,
            "region": region,
            "size": size,
        }
        if backups is not None:
            self._values["backups"] = backups
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if locked is not None:
            self._values["locked"] = locked
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if private_networking is not None:
            self._values["private_networking"] = private_networking
        if resize_disk is not None:
            self._values["resize_disk"] = resize_disk
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data
        if volume_ids is not None:
            self._values["volume_ids"] = volume_ids
        if vpc_uuid is not None:
            self._values["vpc_uuid"] = vpc_uuid

    @builtins.property
    def image(self) -> builtins.str:
        '''The Droplet image ID or slug.

        :schema: CfnDropletProps#Image
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The Droplet name.

        :schema: CfnDropletProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region to start in.

        :schema: CfnDropletProps#Region
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The unique slug that indentifies the type of Droplet.

        You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.

        :schema: CfnDropletProps#Size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backups(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if backups are made.

        Defaults to
        false.

        :default: false.

        :schema: CfnDropletProps#Backups
        '''
        result = self._values.get("backups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if IPv6 is enabled.

        Defaults to false.

        :default: false.

        :schema: CfnDropletProps#Ipv6
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def locked(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDropletProps#Locked
        '''
        result = self._values.get("locked")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def monitoring(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling whether monitoring agent is installed.

        Defaults to false.

        :default: false.

        :schema: CfnDropletProps#Monitoring
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_networking(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if private networking is enabled.

        When VPC is enabled on an account, this will provision the
        Droplet inside of your account's default VPC for the region. Use the
        ``vpc_uuid`` attribute to specify a different VPC.

        :schema: CfnDropletProps#PrivateNetworking
        '''
        result = self._values.get("private_networking")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def resize_disk(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling whether to increase the disk size when resizing a Droplet.

        It defaults to ``true``. When set to ``false``,
        only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk
        size is a permanent change**. Increasing only RAM and CPU is reversible.

        :schema: CfnDropletProps#ResizeDisk
        '''
        result = self._values.get("resize_disk")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``.

        To retrieve this info, use the
        `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_
        or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not
        be added or removed via this provider. Modifying this field will prompt you
        to destroy and recreate the Droplet.

        :schema: CfnDropletProps#SshKeys
        '''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the tags to be applied to this Droplet.

        :schema: CfnDropletProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDropletProps#UserData
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnDropletProps#VolumeIds
        '''
        result = self._values.get("volume_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC where the Droplet will be located.

        :schema: CfnDropletProps#VpcUuid
        '''
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDropletProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDroplet",
    "CfnDropletProps",
]

publication.publish()
