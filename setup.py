from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name="PyPassGenerator",
    version="1.0.0",
    author="Shervin Badanara (shervinbdndev)",
    author_email="shervin2234@gmail.com",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages() ,
    install_requires=[] ,
    keywords=['python', 'password' , 'password generator' , 'strong password'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)