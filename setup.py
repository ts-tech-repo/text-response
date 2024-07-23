"""Setup for TextResponseXBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='text-response-xblock',
    version='0.1',
    description='This XBlock provides an easy way to embed a Encrypt Player.',
    packages=[
        'text-response',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'text-response = text-response:TextResponseXBlock',
        ]
    },
    package_data=package_data("text-response", "static"),
)