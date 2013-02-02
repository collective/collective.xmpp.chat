from distribute_setup import use_setuptools
from setuptools import setup, find_packages
import os

use_setuptools()
version = '0.2b3'

setup(name='collective.xmpp.chat',
      version=version,
      description="XMPP-based instant Messaging for Plone",
      long_description=open("README.txt").read() + "\n" +
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
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.xmpp'],
      package_data={
        'collective.xmpp.chat': [
            'browser/resources/*.*',
            'browser/resources/images/*.*',
            'browser/resources/Libraries/*.*',
            'browser/resources/Libraries/burry.js/burry.js',
            'browser/resources/Libraries/css/jquery-ui-1.9.1.custom/ui-lightness/*.css',
            'browser/resources/Libraries/css/jquery-ui-1.9.1.custom/ui-lightness/images/*.*'
        ]
      },
      exclude_package_data={
        'collective.xmpp.chat': [
            'browser/resources/Libraries/jasmine-1.3.1',
            'browser/resources/Libraries/burry.js',
            'browser/resources/Libraries/spec',
        ],
      },
      zip_safe=False,
      install_requires=[
            'setuptools',
            'collective.xmpp.core',
            'collective.js.jqueryui'
      ],
      extras_require = {
        "sphinx": [ "Sphinx >=1.0",
                    "repoze.sphinx.autointerface",
                  ],
        "test_act": [ 
                    "decorator", 
                    "selenium",
                  ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
