#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: PROJECT_NAME
      @file: setup.py
   @created: DDD, DD Mon YYYY
    @author: AUTHOR_NAME
      @site: SITE_URL
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright (c) 2024, COPYRIGHT

   Reference: https://setuptools.pypa.io/en/latest/references/keywords.html
"""

import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The version of the package
VERSION = (HERE / "tism/.version").read_text().strip()

# The package requirements
REQUIREMENTS = list(filter(None, (HERE / "requirements.txt").read_text().splitlines()))

# This call to setup() does all the work
setuptools.setup(
    name="tism",
    version="0.0.1",
    description="Project description",
    author="AUTHOR_NAME",
    author_email="AUTHOR_EMAIL",
    long_description=README,
    long_description_content_type="text/markdown",
    url="SITE_URL",
    project_urls={"GitHub": "https://github.com/USER/PROJECT_NAME", "PyPi": "https://pypi.org/project/PROJECT_NAME"},
    license="MIT",
    license_files="LICENSE.md",
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Topic :: Terminals",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.10",
    install_requires=REQUIREMENTS,
    keywords="KEYWORDS",
    platforms="Darwin,Linux",
)
