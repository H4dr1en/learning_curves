import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="learning-curve",
    version="0.1.0",
    author="H4dr1en",
    author_email="h4dr1en@pm.me",
    description="Python module allowing to easily calculate and plot the learning curve of a machine learning model and find the maximum expected accuracy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/H4dr1en/learning-curves",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)