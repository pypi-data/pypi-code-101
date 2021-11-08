'''
# AWS CDK CloudFormation Constructs for Generic::Transcribe::Vocabulary

A custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.

## References

* [Source](https://github.com/iann0036/cfn-types/tree/master/generic-transcribe-vocabulary)

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
