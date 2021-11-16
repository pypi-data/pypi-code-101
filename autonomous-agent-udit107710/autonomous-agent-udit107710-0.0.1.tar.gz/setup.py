import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autonomous-agent-udit107710",
    version="0.0.1",
    author="Udit Krishna Chaudhary",
    author_email="uditcry10107@gmail.com",
    description="An autonomous agent to interact with environment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Udit107710/autonomous-agent",
    project_urls={
        "Bug Tracker": "https://github.com/Udit107710/autonomous-agent/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)