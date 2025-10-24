from setuptools import setup, find_packages

setup(
    name="json2pdf",
    version="1.1.0",
    author="Open Developer Community",
    description="Convert JSON files into beautiful, readable PDFs automatically.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["reportlab>=3.6"],
    entry_points={"console_scripts": ["json2pdf=json2pdf.__main__:main"]},
    python_requires=">=3.7",
)
