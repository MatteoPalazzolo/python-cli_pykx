from setuptools import setup, find_packages

setup(
    name="obsidian_pythomation",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["cli"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pykx=cli:main",
        ],
    },
    author="Palazz",
    description="A collection of Python tools to simplify my obsidian workflows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/my_toolbox",
)