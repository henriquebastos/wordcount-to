# coding: utf-8
from setuptools import setup


setup(name='wordcount',
      version='0.1',
      description='Count words.',
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      packages=['wordcount'],
      entry_points={
          'console_scripts': [
              'wordcount = wordcount.__main__:main'
          ]
      },
      zip_safe=False,
      platforms='any',
      include_package_data=False,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],)
