from setuptools import setup

if __name__ == '__main__':

    with open('requirements.txt') as f:
        install_requires = f.read().splitlines()

    setup(name='bundleservice',
          version='1.0',
          description='Service for retrieving and creating bundles of sensor data',
          url='http://github.com/bf6/bundleservice',
          author='Brian Fernandez',
          packages=setuptools.find_packages(),
          install_requires=install_requires,
          )
