from setuptools import setup

version = '0.5.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'simplejson >= 2.3.0, <2.5.0',
    'numpy',
    'Django',
    'django-extensions',
    'django-nose',
    'lizard-ui >= 4.12',
    'lizard-map >= 4.10',
    'numpy',
    'Pillow',
    'pandas',
    'netCDF4',
    'python-dateutil >= 1.5, <2.0',
    'pyproj',
    'GDAL',
    'pydap',
    'factory_boy',
    'mock'
    ],

tests_require = [
    ]

setup(name='lizard-neerslagradar',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_neerslagradar'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
          ],
          'lizard_map.adapter_class': [
     'adapter_neerslagradar = lizard_neerslagradar.layers:NeerslagRadarAdapter'
            ],
          }
      )
