from setuptools import setup

setup(
    name="repodesc",
    version="1.0.0",
    description="Print the description of a Github repository",
    author="Roland Crosby",
    author_email="roland@rolandcrosby.com",
    url="https://github.com/rolandcrosby/repodec",
    entry_points={
        "console_scripts": [
            "repodesc = repodesc:main"
        ]
    },
    packages=["repodesc"],
    install_requires=["requests"]
)
