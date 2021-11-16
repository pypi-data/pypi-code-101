from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='tensorboard-plugin-netron',
    version='0.2.2',
    packages=find_packages(),
    url='https://sr.ht/~dhruvin/tensorboard-plugin-netron',
    license='MIT',
    author='Dhruvin Gandhi',
    author_email='contact@dhruvin.dev',
    description='Netron TensorBoard Plugin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'netron',
        'tensorboard',
        'werkzeug'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'tensorboard_plugins': [
            'netron = tensorboard_plugin_netron:Netron'
        ]
    }
)
