import pkg_resources
import setuptools


def read_requirements(requirements_path):
    with open(requirements_path) as requirements_handle:
        return [
            str(requirement)
            for requirement in pkg_resources.parse_requirements(requirements_handle)
        ]


setuptools.setup(
    name="esp32knife",
    version="0.0.1",
    description="",
    packages=setuptools.find_packages(include=["esp32knife", "esp32knife.*"]),
    install_requires=read_requirements("requirements.txt"),
    python_requires=">=3.7",
)
