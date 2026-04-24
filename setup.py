from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent

long_description = (this_directory / "README.rst").read_text(encoding="utf-8")

setup(
    name="django-cityloc-pkg-dblvsdev",
    version="0.0.5",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)

