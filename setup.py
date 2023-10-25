from setuptools import setup, find_packages

with open("pennylane_sphinx_theme/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")


requirements = [
    "sphinx",
    "xanadu-sphinx-theme~=0.5.0",
    # The packages below are used to generate thumbnail images.
    "pillow",
    "sphinx-gallery",
    "docutils",
]

info = {
    "description": "Sphinx theme for PennyLane open-source Python packages",
    "entry_points": {"sphinx.html_themes": ["pennylane = pennylane_sphinx_theme"]},
    "maintainer": "Xanadu Inc.",
    "maintainer_email": "software@xanadu.ai",
    "install_requires": requirements,
    "license": "Apache License 2.0",
    "license_files": ["LICENSE"],
    "long_description": open("README.rst").read(),
    "long_description_content_type": "text/x-rst",
    "include_package_data": True,
    "name": "pennylane-sphinx-theme",
    "packages": find_packages(where="."),
    "package_data": {"pennylane_sphinx_theme": ["static/*", "*.html", "theme.conf"]},
    "provides": ["pennylane_sphinx_theme"],
    "url": "https://github.com/XanaduAI/pennylane-sphinx-theme",
    "version": version,
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
]


setup(classifiers=classifiers, **info)
