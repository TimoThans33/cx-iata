import setuptools

setuptools.setup(
    name="cx-iata-t2",
    version="1.0",
    author="timo",
    author_email="t.thans@primevision.com",
    description="customer experience for analysing IATA data",
    url="https://github.com/TimoThans33/cx-iata",
    packages=['app'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'PyQt5'
    ],
    python_requires='==3.6',
)