'''
# custom-cloud9-ssm

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|[`cdk_use_cases.custom_cloud9_ssm`](https://pypi.org/project/cdk-use-cases.custom-cloud9-ssm/)|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|[`@cdk-use-cases/custom-cloud9-ssm`](https://www.npmjs.com/package/@cdk-use-cases/custom-cloud9-ssm)|

This pattern implements a Cloud9 EC2 environment, applying an initial configuration to the EC2 instance using an SSM Document. It includes helper methods to add steps and parameters to the SSM Document and to resize the EBS volume of the EC2 instance to a given size.

Here is a minimal deployable pattern definition in Typescript:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CustomCloud9Ssm(stack, "CustomCloud9Ssm")
```

You can view [other usage examples](#other-usage-examples).

## Initializer

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CustomCloud9Ssm(scope, Construct, id, string, props, CustomCloud9SsmProps)
```

*Parameters*

* scope [`Construct`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.Construct.html)
* id `string`
* props [`CustomCloud9SsmProps`](#pattern-construct-props)

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
| ssmDocumentProps? | [ssm.CfnDocumentProps](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ssm.CfnDocumentProps.html) | Optional configuration for the SSM Document. |
| cloud9Ec2Props? | [cloud9.Ec2EnvironmentProps](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-cloud9.Ec2EnvironmentProps.html) | Optional configuration for the Cloud9 EC2 environment. |

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
| ec2Role | [iam.Role](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-iam.Role.html) | The IAM Role that is attached to the EC2 instance launched with the Cloud9 environment to grant it permissions to execute the statements in the SSM Document. |

## Pattern Methods

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
add_document_steps(steps, string)
```

*Description*

Adds one or more steps to the content of the SSM Document.

*Parameters*

* steps `string`: YAML formatted string containing one or more steps to be added to the `mainSteps` section of the SSM Document.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
add_document_parameters(parameters, string)
```

*Description*

Adds one or more parameters to the content of the SSM Document.

*Parameters*

* parameters `string`: YAML formatted string containing one or more parameters to be added to the `parameters` section of the SSM Document.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
resize_eBSTo(size, number)
```

*Description*

Adds a step to the SSM Document content that resizes the EBS volume of the EC2 instance. Attaches the required policies to `ec2Role`.

*Parameters*

* size `number`: size in GiB to resize the EBS volume to.

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Cloud9 EC2 environment

* Creates a Cloud9 EC2 environment with:

  * New VPC that spans 2 AZs and has one public and private subnet per AZ.
  * T2.micro instance type.

### SSM Document

* Creates an SSM Document with:

  * A step that installs jq.
  * A step that resizes the EBS volume of the EC2 instance to 100 GiB.

## Architecture

![Architecture Diagram](architecture.png)

## Other usage examples

*Using default configuration and adding steps*

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_use_cases.custom_cloud9_ssm import CustomCloud9Ssm

# Define a step that installs boto3
boto3_step = """
- name: InstallBoto3
  action: aws:runShellScript
  inputs:
    runCommand:
    - "#!/bin/bash"
    - sudo pip install boto3
"""

# Create the custom environment
custom_cloud9 = CustomCloud9Ssm(self, "CustomCloud9Ssm")

# Add your step to the default document configuration
custom_cloud9.add_document_steps(boto3_step)
```

*Providing props for the SSM Document and resizing the EBS volume*

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_use_cases.custom_cloud9_ssm import CustomCloud9Ssm, CustomCloud9SsmProps
yaml = require("yaml")

# Define the content of the document
content = """
schemaVersion: '2.2'
description: Bootstrap Cloud9 EC2 instance
mainSteps:
- name: InstallBoto3
  action: aws:runShellScript
  inputs:
    runCommand:
    - "#!/bin/bash"
    - sudo pip install boto3
"""

# Specify the configuration for the SSM Document
cloud9_props = {
    "ssm_document_props": {
        "document_type": "Command",
        "content": yaml.parse(content),
        "name": "MyDocument"
    }
}

# Create the custom environment
custom_cloud9 = CustomCloud9Ssm(self, "CustomCloud9Ssm", cloud9_props)

# Add a step to resize the EBS volume to 50GB
custom_cloud9.resize_eBSTo(50)
```

---


© Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import aws_cdk.aws_cloud9
import aws_cdk.aws_iam
import aws_cdk.aws_ssm
import aws_cdk.core


class CustomCloud9Ssm(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-use-cases/custom-cloud9-ssm.CustomCloud9Ssm",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cloud9_ec2_props: typing.Optional[aws_cdk.aws_cloud9.Ec2EnvironmentProps] = None,
        ssm_document_props: typing.Optional[aws_cdk.aws_ssm.CfnDocumentProps] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cloud9_ec2_props: (experimental) Optional configuration for the Cloud9 EC2 environment. Default: : none
        :param ssm_document_props: (experimental) Optional configuration for the SSM Document. Default: : none

        :stability: experimental
        '''
        props = CustomCloud9SsmProps(
            cloud9_ec2_props=cloud9_ec2_props, ssm_document_props=ssm_document_props
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDocumentParameters")
    def add_document_parameters(self, parameters: builtins.str) -> None:
        '''(experimental) Adds one or more parameters to the content of the SSM Document.

        :param parameters: : YAML formatted string containing one or more parameters to be added to the parameters section of the SSM Document.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDocumentParameters", [parameters]))

    @jsii.member(jsii_name="addDocumentSteps")
    def add_document_steps(self, steps: builtins.str) -> None:
        '''(experimental) Adds one or more steps to the content of the SSM Document.

        :param steps: : YAML formatted string containing one or more steps to be added to the mainSteps section of the SSM Document.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDocumentSteps", [steps]))

    @jsii.member(jsii_name="resizeEBSTo")
    def resize_ebs_to(self, size: jsii.Number) -> None:
        '''(experimental) Adds a step to the SSM Document content that resizes the EBS volume of the EC2 instance.

        Attaches the required policies to ec2Role.

        :param size: : size in GiB to resize the EBS volume to.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "resizeEBSTo", [size]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2Role")
    def ec2_role(self) -> aws_cdk.aws_iam.Role:
        '''(experimental) The IAM Role that is attached to the EC2 instance launched with the Cloud9 environment to grant it permissions to execute the statements in the SSM Document.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.Role, jsii.get(self, "ec2Role"))


@jsii.data_type(
    jsii_type="@cdk-use-cases/custom-cloud9-ssm.CustomCloud9SsmProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloud9_ec2_props": "cloud9Ec2Props",
        "ssm_document_props": "ssmDocumentProps",
    },
)
class CustomCloud9SsmProps:
    def __init__(
        self,
        *,
        cloud9_ec2_props: typing.Optional[aws_cdk.aws_cloud9.Ec2EnvironmentProps] = None,
        ssm_document_props: typing.Optional[aws_cdk.aws_ssm.CfnDocumentProps] = None,
    ) -> None:
        '''
        :param cloud9_ec2_props: (experimental) Optional configuration for the Cloud9 EC2 environment. Default: : none
        :param ssm_document_props: (experimental) Optional configuration for the SSM Document. Default: : none

        :stability: experimental
        '''
        if isinstance(cloud9_ec2_props, dict):
            cloud9_ec2_props = aws_cdk.aws_cloud9.Ec2EnvironmentProps(**cloud9_ec2_props)
        if isinstance(ssm_document_props, dict):
            ssm_document_props = aws_cdk.aws_ssm.CfnDocumentProps(**ssm_document_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud9_ec2_props is not None:
            self._values["cloud9_ec2_props"] = cloud9_ec2_props
        if ssm_document_props is not None:
            self._values["ssm_document_props"] = ssm_document_props

    @builtins.property
    def cloud9_ec2_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloud9.Ec2EnvironmentProps]:
        '''(experimental) Optional configuration for the Cloud9 EC2 environment.

        :default: : none

        :stability: experimental
        '''
        result = self._values.get("cloud9_ec2_props")
        return typing.cast(typing.Optional[aws_cdk.aws_cloud9.Ec2EnvironmentProps], result)

    @builtins.property
    def ssm_document_props(self) -> typing.Optional[aws_cdk.aws_ssm.CfnDocumentProps]:
        '''(experimental) Optional configuration for the SSM Document.

        :default: : none

        :stability: experimental
        '''
        result = self._values.get("ssm_document_props")
        return typing.cast(typing.Optional[aws_cdk.aws_ssm.CfnDocumentProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomCloud9SsmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CustomCloud9Ssm",
    "CustomCloud9SsmProps",
]

publication.publish()
