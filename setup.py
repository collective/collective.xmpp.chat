from distribute_setup import use_setuptools
from setuptools import setup, find_packages
import os

use_setuptools()
version = '0.3.2.dev0'

setup(
    name='collective.xmpp.chat',
    version=version,
    description="XMPP-based instant Messaging for Plone",
    long_description=open("README.rst").read() + "\n" +
                open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
    "Framework :: Plone",
    "Programming Language :: Python",
    ],
    keywords='xmpp chat messaging',
    author='JC Brand',
    author_email='jc@opkode.com',
    url='https://github.com/collective/collective.xmpp.chat',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.xmpp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.jquery>=1.7.2',
        'setuptools',
        'collective.xmpp.core',
    ],
    extras_require={
        "sphinx": [
            "Sphinx>=1.0",
            "repoze.sphinx.autointerface",
        ],
        "test": ['plone.app.testing[robot]'],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    setup_requires=["PasteScript", "setuptools_git>=0.3"],
    paster_plugins=["ZopeSkel"],
)
