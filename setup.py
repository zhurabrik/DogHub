from pkg_resources import parse_requirements
from setuptools import find_packages, setup


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, "r") as fp:
        for req in parse_requirements(fp.read()):
            extras = "[{}]".format(",".join(req.extras)) if req.extras else ""
            requirements.append(
                "{}{}{}".format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name="dogshub-api",
    platforms="all",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "dogshub-api = backend.__main__:main",
        ]
    },
)
