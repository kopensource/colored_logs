import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colored_logs",
    version="0.2.9",
    author="Kovacs Kristof-Attila",
    description="A colored logs package based on 'colored'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/ColoredLogs",
    packages=setuptools.find_packages(),
    install_requires=[""],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)