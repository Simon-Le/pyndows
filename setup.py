import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, "README.md"), "r") as f:
    long_description = f.read()

setup(
    name="pyndows",
    version=open("pyndows/version.py").readlines()[-1].split()[-1].strip("\"'"),
    author="Colin Bounouar",
    author_email="colin.bounouar.dev@gmail.com",
    maintainer="Colin Bounouar",
    maintainer_email="colin.bounouar.dev@gmail.com",
    url="https://colin-b.github.io/pyndows/",
    description="Accessing Windows from Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://pypi.org/project/pyndows/",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords=["windows", "samba", "linux", "remote"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=["pysmb==1.*"],
    extras_require={
        "testing": [
            # Used to launch tests and check coverage
            "pytest-cov==2.*",
        ]
    },
    python_requires=">=3.6",
    project_urls={
        "GitHub": "https://github.com/Colin-b/pyndows",
        "Changelog": "https://github.com/Colin-b/pyndows/blob/master/CHANGELOG.md",
        "Issues": "https://github.com/Colin-b/pyndows/issues",
    },
    platforms=["Windows", "Linux"],
)
