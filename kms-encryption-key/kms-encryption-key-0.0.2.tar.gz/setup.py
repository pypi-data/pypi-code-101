import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "kms-encryption-key",
    "version": "0.0.2",
    "description": "CDK Construct to create KMS Key with defined Administrator Role Arns",
    "license": "Apache-2.0",
    "url": "https://github.com/jadecobra/kms-encryption-key.git",
    "long_description_content_type": "text/markdown",
    "author": "jakeitegsy<jakeitegsy@yahoo.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/jadecobra/kms-encryption-key.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "kms_encryption_key",
        "kms_encryption_key._jsii"
    ],
    "package_data": {
        "kms_encryption_key._jsii": [
            "kms-encryption-key@0.0.2.jsii.tgz"
        ],
        "kms_encryption_key": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-iam>=1.95.2, <2.0.0",
        "aws-cdk.aws-kms>=1.95.2, <2.0.0",
        "aws-cdk.core>=1.95.2, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.42.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
