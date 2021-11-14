from setuptools import setup, find_packages

with open('readme.md', 'r') as f :
    readme_content = f.read()

setup(
    name='petit_recipe_executor',
    version='0.1.0',
    description='Execute simple recipes to test small things',
    packages=find_packages(),
    url='https://github.com/Plawn/petit_recipe_executor',
    license='apache-2.0',
    author='Plawn',
    author_email='plawn.yay@gmail.com',
    long_description=readme_content,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    install_requires=['requests', 'pydantic'],
)
