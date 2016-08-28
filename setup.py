from setuptools import setup, find_packages

setup(name='djangocms-light-gallery',
      version='0.1',
      description='',
      url='https://github.com/andyklimczak/djangocms-light-gallery',
      author='Andy Klimczak',
      author_email='andyklimczak@fastmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'django>=1.6',
          'django-cms>=3.0',
          'django-filer',
          'django-sekizai',
          'easy-thumbnails'
      ],
      zip_safe=False)
