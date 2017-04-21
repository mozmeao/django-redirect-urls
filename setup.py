import codecs
import os.path
import re
from setuptools import setup


def find_version(*file_paths):
    version_file = codecs.open(os.path.join(os.path.dirname(__file__),
                               *file_paths), 'rb', encoding='utf8').read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-redirect-urls',
    version=find_version('redirect_urls', '__init__.py'),
    description='URL redirecting and rewriting in code.',
    long_description=open('README.md').read(),
    author='Paul McLanahan',
    author_email='pmac@mozilla.com',
    url='https://github.com/pmac/django-redirect-urls/',
    license='Apache-2.0',
    packages=['redirect_urls'],
    include_package_data=True,
    zip_safe=False,
    keywords='django redirects',
    install_requires=['Django>=1.8'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
