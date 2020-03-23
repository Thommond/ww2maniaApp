import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="ww2mania"
    version="0.0.1",
    author="Thom J Mondeaux",
    author_email="Thommond@protonmail.com",
    url="https://github.com/Thommond/ww2maniaApp",
    description="Text adventure turned into a app, more details on read me.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
