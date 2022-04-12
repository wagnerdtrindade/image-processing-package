from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="wagner_trindade",
    author_email="wagner.d.trindade@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wagnerdtrindade/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)