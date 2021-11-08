import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-cloudformation-atlassian-opsgenie-team",
    "version": "1.0.1.a1",
    "description": "Opsgenie Team resource schema",
    "license": "Apache-2.0",
    "url": "https://github.com/opsgenie/opsgenie-cloudformation-resources",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cdk-cloudformation.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_cloudformation_atlassian_opsgenie_team",
        "cdk_cloudformation_atlassian_opsgenie_team._jsii"
    ],
    "package_data": {
        "cdk_cloudformation_atlassian_opsgenie_team._jsii": [
            "atlassian-opsgenie-team@1.0.1-alpha.1.jsii.tgz"
        ],
        "cdk_cloudformation_atlassian_opsgenie_team": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.core>=1.131.0, <2.0.0",
        "constructs>=3.3.161, <4.0.0",
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
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
