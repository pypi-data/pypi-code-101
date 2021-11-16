# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sevivi',
 'sevivi.config',
 'sevivi.config.config_types',
 'sevivi.image_provider',
 'sevivi.image_provider.graph_provider',
 'sevivi.image_provider.video_provider',
 'sevivi.image_provider.video_provider.video_imu_capture_app',
 'sevivi.synchronizer',
 'sevivi.video_renderer']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2,<9.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'numpy>=1.21.3,<2.0.0',
 'opencv-python>=4.5.4.58,<5.0.0.0',
 'pandas>=1.3.4,<2.0.0',
 'read-protobuf>=0.1.1,<0.2.0',
 'scipy>=1.7.1,<2.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['sevivi = sevivi.main:run']}

setup_kwargs = {
    'name': 'sevivi',
    'version': '1.0.3',
    'description': 'Create a video with graphs synchronous to a source video',
    'long_description': None,
    'author': 'Justin Albert',
    'author_email': 'justin.albert@hpi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hpi-dhc/sevivi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
