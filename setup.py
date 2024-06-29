
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.11'
DESCRIPTION = 'NetworkEyuel integration'
LONG_DESCRIPTION = 'This package is a helper package with NetworkEyuel integration.'

# Setting up
setup(
    name="networkeyuel",
    version=VERSION,
    author="network-eyu",
    author_email="<networkeyuel@duck.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests', 'cryptography'],
    keywords=['python', 'networkeyuel', 'payment', 'ethiopia', 'ethio telecom'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
