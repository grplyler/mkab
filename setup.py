from setuptools import setup, find_packages

setup(
    name="mkab",
    description="A Command line tool to generate audiobooks with AWS and Google Cloud Services",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "click",   
        "google-cloud-texttospeech",
        "coloredlogs"     
    ],
    entry_points={
        "console_scripts": [
            "mkab = mkab.cli:cli"
        ]
    },
)