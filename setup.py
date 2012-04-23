from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='example.wtforms',
      version=version,
      description="Some test and examples of collective.wtforms",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone wtforms form example',
      author='keul',
      author_email='luca@keul.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['example'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.wtforms',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
