'''
# AWS Lambda Layer with the NPM dependency proxy-agent

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module exports a single class called `NodeProxyAgentLayer` which is a `lambda.Layer` that bundles the NPM dependency [`proxy-agent`](https://www.npmjs.com/package/proxy-agent).

> * proxy-agent Version: 5.0.0

Usage:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
fn = lambda_.Function(...)
fn.add_layers(NodeProxyAgentLayer(stack, "NodeProxyAgentLayer"))
```

[`proxy-agent`](https://www.npmjs.com/package/proxy-agent) will be installed under `/opt/nodejs/node_modules`.
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

import aws_cdk.aws_lambda
import constructs


class NodeProxyAgentLayer(
    aws_cdk.aws_lambda.LayerVersion,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/lambda-layer-node-proxy-agent.NodeProxyAgentLayer",
):
    '''An AWS Lambda layer that includes the NPM dependency ``proxy-agent``.'''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "NodeProxyAgentLayer",
]

publication.publish()
