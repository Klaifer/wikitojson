import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wikitojson",
    version="0.0.1",
    author="Klaifer Garcia",
    description="Wikipedia(English) to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["wikitojson"],
    package_dir={'':'wikitojson/src'},
    install_requires=[]
)