from setuptools import setup


setup(name='cyclopes',
      version='1.0',
      description='README.md',
      author='Raghav, Charan',
      packages=['cyclopes'],
      install_requires=['tensorflow==1.12.0',
                        'numpy==1.15.4',
                        'librosa==0.6.2'],
      )
