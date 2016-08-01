from setuptools import setup

setup(name='conj',
      version='1.4.2',
      description='Python conjugation module for Turkish',
      url='https://github.com/halilkaya/conj',
      author='Halil Kaya',
      author_email='halil@halilkaya.net',
      license='GPLv3',
      packages=['conj'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: Turkish',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
      ],
      scripts=['conj/__init__.py'],
      install_requires=['setuptools'],
      zip_safe=False)
