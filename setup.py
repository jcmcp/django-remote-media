from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-remote-media',
    version='0.1',
    url='https://github.com/jcmcp/django-remote-media',
    license='MIT',
    author='John McPherson',
    author_email='jcmcph@gmail.com',
    description='Save remote files to django FileField or ImageField',
    long_description=readme(),
)