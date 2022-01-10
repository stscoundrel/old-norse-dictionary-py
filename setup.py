import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="old-norse-dictionary",
    version="1.0.0",
    author="stscoundrel",
    description="Old Norse Dictionary for Python. From The Cleasby & Vigfusson Old Norse to English Dictionary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/old-norse-dictionary-py",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    package_data={"": ["**/*.json"]},
)
