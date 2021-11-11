import setuptools

setuptools.setup(
    name="streamlit_text_like",
    version="0.0.2",
    author="Ashish Rai",
    author_email="ashishraics512@gmail.com",
    description="streamlit_text_like enables to like or dislike a text input",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/PROFESSOR-PENGUIN/streamlit-text-like",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
