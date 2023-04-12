from setuptools import setup, find_packages

setup(
    name="InstaReq",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "instareq = instareq:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mubarak Alketbi",
    author_email="mubarak.harran@gmail.com",
    url="https://github.com/MHketbi/InstaReq",
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
