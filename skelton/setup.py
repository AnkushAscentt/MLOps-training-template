import setuptools

setuptools.setup(
    name="tmna-${{ values.pod-name }}",
    version="1.0.0",
    author="{{ cookiecutter.author }}",
    description="This is TDSP sample implementation",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="OSI Approved :: MIT License",
    platforms=["OS Independent"],
    setup_requires=["pytest-runner"],
)
