import os
from setuptools import setup, find_packages
import honeypot-signals


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="honeypot-signals",
    version=honeypot-signals.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='admin_honeypot, admin-honeypot, honeypot, signals, email',
    packages=find_packages(),
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="http://www.github.com/bitmazk/django-honeypot-signals",
    include_package_data=True,
    test_suite='honeypot-signals.tests.runtests.runtests',
)
