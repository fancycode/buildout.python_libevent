try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup, find_packages

import version

setup(
    name = 'buildout.python_libevent',
    version = version.get_git_version(),
    description = "Buildout recipe for python-libevent",
    author = "Joachim Bauch",
    author_email = "mail@joachim-bauch.de",
    url = "http://www.joachim-bauch.de/projects/python-libevent/",
    download_url = "http://pypi.python.org/pypi/buildout.python_libevent/",
    keywords = "buildout recipe libevent",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages = ['buildout'],
    entry_points = {
        'zc.buildout': [
            'default = buildout.python_libevent:Recipe',
        ],
    },
    dependency_links = [
        'http://pypi.python.org/simple/zc.recipe.egg',
    ],
    install_requires = [
        'setuptools',
        'zc.recipe.egg',
    ],
)
