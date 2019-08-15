from setuptools import setup

with open('README.md', 'r') as f:
    markdown_str = f.read()

setup(name='Boruta-Ingvar-Y',
      version='0.3',
      description='Python Implementation of Boruta Feature Selection',
      long_description=markdown_str,
      long_description_content_type='text/markdown',
      url='https://github.com/scikit-learn-contrib/boruta_py',
      author='Daniel Homola',
      author_email='dani.homola@gmail.com',
      license='BSD-3-Clause',
      packages=['boruta'],
      package_dir={'boruta': 'boruta'},
      package_data={'boruta': ['boruta/examples/*.csv']},
      include_package_data = True,
      keywords=['feature selection', 'machine learning', 'random forest'],
      install_requires=['numpy>=1.10.4',
                        'scikit-learn>=0.17.1',
                        'scipy>=0.17.0'
                       ],
      classifiers=['License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent'
                  ])
