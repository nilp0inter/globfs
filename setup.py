from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.md')).read()
CHANGELOG = open(os.path.join(HERE, 'CHANGELOG.txt')).read()

VERSION = '0.0.1'

setup(name='globfs',
      version=VERSION,
      description="Unionfs-like FUSE with branch selection based on glob patterns.",
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='unionfs aufs glob fuse',
      author='Roberto Abdelkader Mart\xc3\xadnez P\xc3\xa9rez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/nilp0inter/globfs',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,)
