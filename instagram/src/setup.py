# setup.py to init the project

from setuptools import setup, find_packages


setup(
    name="instagram_bot",
    version="0.1.0",
    description="A Python package to automate Instagram actions.",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "python-dotenv",
        "requests",
        "beautifulsoup4",
        "lxml",
    ],
    entry_points={"console_scripts": ["instagram=instagram.main:main"]},
)
