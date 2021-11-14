import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name                          = "squares",
    version                       = "0.0.1",
    author                        = "Alee",
    author_email                  = "mazaeela@gmail.com",
    description                   = "An identicon generator",
    license                       = "MIT",
    keywords                      = ["identicon", "pil"],
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/aaeg/squares",
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    packages                      = ["squares"],
    install_requires              = ["pillow>=8.1.0"],
)
