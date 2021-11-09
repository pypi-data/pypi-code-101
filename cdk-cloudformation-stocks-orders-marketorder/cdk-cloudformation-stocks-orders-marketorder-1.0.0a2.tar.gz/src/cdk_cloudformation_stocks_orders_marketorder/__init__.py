'''
# stocks-orders-marketorder

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Stocks::Orders::MarketOrder` v1.0.0.

## Description

A market order is a request to buy or sell a security at the currently available market price. The order to buy a security will be submitted on resource creation and the security will be sold (or the unfilled order cancelled) on resource deletion. Supported exchanges are AMEX, ARCA, BATS, NYSE, NASDAQ and NYSEARCA.

## References

* [Source](https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Stocks::Orders::MarketOrder \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/Stocks-Orders-MarketOrder \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Stocks::Orders::MarketOrder`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fstocks-orders-marketorder+v1.0.0).
* Issues related to `Stocks::Orders::MarketOrder` should be reported to the [publisher](https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder).

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


class CfnMarketorder(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/stocks-orders-marketorder.CfnMarketorder",
):
    '''A CloudFormation ``Stocks::Orders::MarketOrder``.

    :cloudformationResource: Stocks::Orders::MarketOrder
    :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        quantity: jsii.Number,
        symbol: builtins.str,
        notes: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Stocks::Orders::MarketOrder``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param quantity: The number of shares to buy.
        :param symbol: The stock symbol to buy.
        :param notes: A fields for notes about the order. This field may also be used to force a resource update in order to retrieve the latest market value of the position.
        '''
        props = CfnMarketorderProps(quantity=quantity, symbol=symbol, notes=notes)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCurrentValue")
    def attr_current_value(self) -> builtins.str:
        '''Attribute ``Stocks::Orders::MarketOrder.CurrentValue``.

        :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFilledAt")
    def attr_filled_at(self) -> builtins.str:
        '''Attribute ``Stocks::Orders::MarketOrder.FilledAt``.

        :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFilledAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFilledQuantity")
    def attr_filled_quantity(self) -> builtins.str:
        '''Attribute ``Stocks::Orders::MarketOrder.FilledQuantity``.

        :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFilledQuantity"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFilledValue")
    def attr_filled_value(self) -> builtins.str:
        '''Attribute ``Stocks::Orders::MarketOrder.FilledValue``.

        :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFilledValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Stocks::Orders::MarketOrder.Id``.

        :link: https://github.com/iann0036/cfn-types/tree/master/stocks-orders-marketorder
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMarketorderProps":
        '''Resource props.'''
        return typing.cast("CfnMarketorderProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stocks-orders-marketorder.CfnMarketorderProps",
    jsii_struct_bases=[],
    name_mapping={"quantity": "quantity", "symbol": "symbol", "notes": "notes"},
)
class CfnMarketorderProps:
    def __init__(
        self,
        *,
        quantity: jsii.Number,
        symbol: builtins.str,
        notes: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A market order is a request to buy or sell a security at the currently available market price.

        The order to buy a security will be submitted on resource creation and the security will be sold (or the unfilled order cancelled) on resource deletion. Supported exchanges are AMEX, ARCA, BATS, NYSE, NASDAQ and NYSEARCA.

        :param quantity: The number of shares to buy.
        :param symbol: The stock symbol to buy.
        :param notes: A fields for notes about the order. This field may also be used to force a resource update in order to retrieve the latest market value of the position.

        :schema: CfnMarketorderProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "quantity": quantity,
            "symbol": symbol,
        }
        if notes is not None:
            self._values["notes"] = notes

    @builtins.property
    def quantity(self) -> jsii.Number:
        '''The number of shares to buy.

        :schema: CfnMarketorderProps#Quantity
        '''
        result = self._values.get("quantity")
        assert result is not None, "Required property 'quantity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def symbol(self) -> builtins.str:
        '''The stock symbol to buy.

        :schema: CfnMarketorderProps#Symbol
        '''
        result = self._values.get("symbol")
        assert result is not None, "Required property 'symbol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''A fields for notes about the order.

        This field may also be used to force a resource update in order to retrieve the latest market value of the position.

        :schema: CfnMarketorderProps#Notes
        '''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMarketorderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMarketorder",
    "CfnMarketorderProps",
]

publication.publish()
