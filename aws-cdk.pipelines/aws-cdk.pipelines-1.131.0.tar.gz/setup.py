import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.pipelines",
    "version": "1.131.0",
    "description": "Continuous Delivery of CDK applications",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.pipelines",
        "aws_cdk.pipelines._jsii"
    ],
    "package_data": {
        "aws_cdk.pipelines._jsii": [
            "pipelines@1.131.0.jsii.tgz"
        ],
        "aws_cdk.pipelines": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-codebuild==1.131.0",
        "aws-cdk.aws-codecommit==1.131.0",
        "aws-cdk.aws-codepipeline-actions==1.131.0",
        "aws-cdk.aws-codepipeline==1.131.0",
        "aws-cdk.aws-ec2==1.131.0",
        "aws-cdk.aws-ecr==1.131.0",
        "aws-cdk.aws-events==1.131.0",
        "aws-cdk.aws-iam==1.131.0",
        "aws-cdk.aws-lambda==1.131.0",
        "aws-cdk.aws-s3-assets==1.131.0",
        "aws-cdk.aws-s3==1.131.0",
        "aws-cdk.aws-secretsmanager==1.131.0",
        "aws-cdk.aws-sns==1.131.0",
        "aws-cdk.cloud-assembly-schema==1.131.0",
        "aws-cdk.core==1.131.0",
        "aws-cdk.cx-api==1.131.0",
        "constructs>=3.3.69, <4.0.0",
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
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
