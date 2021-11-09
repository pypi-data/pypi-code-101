'''
# generic-transcribe-vocabulary

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Generic::Transcribe::Vocabulary` v1.0.0.

## Description

A custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.

## References

* [Source](https://github.com/iann0036/cfn-types/tree/master/generic-transcribe-vocabulary)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Generic::Transcribe::Vocabulary \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/Generic-Transcribe-Vocabulary \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Generic::Transcribe::Vocabulary`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fgeneric-transcribe-vocabulary+v1.0.0).
* Issues related to `Generic::Transcribe::Vocabulary` should be reported to the [publisher](https://github.com/iann0036/cfn-types/tree/master/generic-transcribe-vocabulary).

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


class CfnVocabulary(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/generic-transcribe-vocabulary.CfnVocabulary",
):
    '''A CloudFormation ``Generic::Transcribe::Vocabulary``.

    :cloudformationResource: Generic::Transcribe::Vocabulary
    :link: https://github.com/iann0036/cfn-types/tree/master/generic-transcribe-vocabulary
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Generic::Transcribe::Vocabulary``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param language_code: The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see `What is Amazon Transcribe? <https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html>`_.
        :param vocabulary_name: The name of the vocabulary. The name must be unique within an AWS account. The name is case sensitive.
        :param phrases: An array of strings that contains the vocabulary entries.
        :param vocabulary_file_uri: The S3 location of the text file that contains the definition of the custom vocabulary. The URI must be in the same region as the API endpoint that you are calling.
        '''
        props = CfnVocabularyProps(
            language_code=language_code,
            vocabulary_name=vocabulary_name,
            phrases=phrases,
            vocabulary_file_uri=vocabulary_file_uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnVocabularyProps":
        '''Resource props.'''
        return typing.cast("CfnVocabularyProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-transcribe-vocabulary.CfnVocabularyProps",
    jsii_struct_bases=[],
    name_mapping={
        "language_code": "languageCode",
        "vocabulary_name": "vocabularyName",
        "phrases": "phrases",
        "vocabulary_file_uri": "vocabularyFileUri",
    },
)
class CfnVocabularyProps:
    def __init__(
        self,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.

        :param language_code: The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see `What is Amazon Transcribe? <https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html>`_.
        :param vocabulary_name: The name of the vocabulary. The name must be unique within an AWS account. The name is case sensitive.
        :param phrases: An array of strings that contains the vocabulary entries.
        :param vocabulary_file_uri: The S3 location of the text file that contains the definition of the custom vocabulary. The URI must be in the same region as the API endpoint that you are calling.

        :schema: CfnVocabularyProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "language_code": language_code,
            "vocabulary_name": vocabulary_name,
        }
        if phrases is not None:
            self._values["phrases"] = phrases
        if vocabulary_file_uri is not None:
            self._values["vocabulary_file_uri"] = vocabulary_file_uri

    @builtins.property
    def language_code(self) -> builtins.str:
        '''The language code of the vocabulary entries.

        For a list of languages and their corresponding language codes, see `What is Amazon Transcribe? <https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html>`_.

        :schema: CfnVocabularyProps#LanguageCode
        '''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vocabulary_name(self) -> builtins.str:
        '''The name of the vocabulary.

        The name must be unique within an AWS account. The name is case sensitive.

        :schema: CfnVocabularyProps#VocabularyName
        '''
        result = self._values.get("vocabulary_name")
        assert result is not None, "Required property 'vocabulary_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phrases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings that contains the vocabulary entries.

        :schema: CfnVocabularyProps#Phrases
        '''
        result = self._values.get("phrases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vocabulary_file_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 location of the text file that contains the definition of the custom vocabulary.

        The URI must be in the same region as the API endpoint that you are calling.

        :schema: CfnVocabularyProps#VocabularyFileUri
        '''
        result = self._values.get("vocabulary_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVocabularyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVocabulary",
    "CfnVocabularyProps",
]

publication.publish()
