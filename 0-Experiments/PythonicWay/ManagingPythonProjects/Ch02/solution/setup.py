from setuptools import setup
import re


with open('README.md') as fp:
    long_description = fp.read()


def find_version():
    with open('nlp/__init__.py') as fp:
        for line in fp:
            # __version__ = '0.1.0'
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    assert False, 'cannot find version'


setup(
    name='slowmath',
    version=find_version(),
    packages=['slowmath'],
    description='Math for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    maintainer='You',
    maintainer_email='you@yourcompany.com',
    url='https://github.com/yourcompany/slowmath',
)
