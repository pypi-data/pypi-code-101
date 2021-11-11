from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setup(
        name='rule34api',
        version=0.1,
        description='Unofficial Rule34 API',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='MoMMde',
        license='MIT',
        keywords=['rule34', 'porn', 'api', 'wrapper', 'nudity', 'requests', 'http'],
        author_email='mommde@pm.me',
        install_requires=['xmltodict', 'dataclasses-json'],
        url='https://github.com/hide-and-hentai/rule34-api'
    )
