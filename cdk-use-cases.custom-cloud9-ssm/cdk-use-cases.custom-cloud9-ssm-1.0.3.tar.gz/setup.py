import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-use-cases.custom-cloud9-ssm",
    "version": "1.0.3",
    "description": "Pattern for Cloud9 EC2 environment and SSM Document.",
    "license": "Apache-2.0",
    "url": "https://github.com/aws-samples/cdk-use-cases.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws-samples/cdk-use-cases.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_use_cases.custom_cloud9_ssm",
        "cdk_use_cases.custom_cloud9_ssm._jsii"
    ],
    "package_data": {
        "cdk_use_cases.custom_cloud9_ssm._jsii": [
            "custom-cloud9-ssm@1.0.3.jsii.tgz"
        ],
        "cdk_use_cases.custom_cloud9_ssm": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-cloud9>=1.132.0, <2.0.0",
        "aws-cdk.aws-ec2>=1.132.0, <2.0.0",
        "aws-cdk.aws-iam>=1.132.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.132.0, <2.0.0",
        "aws-cdk.aws-ssm>=1.132.0, <2.0.0",
        "aws-cdk.core==1.132.0",
        "constructs>=3.3.161, <4.0.0",
        "jsii>=1.43.0, <2.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": [
        "src/cdk_use_cases/custom_cloud9_ssm/_jsii/bin/custom-cloud9-ssm"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
