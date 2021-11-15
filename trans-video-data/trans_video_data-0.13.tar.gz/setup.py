"""
@File: None
@Author: Jackpot
@Date: None
@Description: None
@email: wikileaks928@gmail.com
"""
import setuptools

install_requires = [
    'grpcio==1.41.1',
    'grpc==1.0.0',
    'protobuf==3.19.1'
]

setuptools.setup(
    name='trans_video_data',
    version='0.13',
    author='jackpot',
    packages=['db-controllers'],
    install_requires=install_requires
)
