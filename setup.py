# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.base',
    version=version,
    description="The core code to support GroupServer groups",
    long_description=open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='user, group, page',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.app.content',
        'zope.cachedescriptors',
        'zope.component',
        'zope.interface',
        'zope.schema',
        'AccessControl',
        'gs.content.base',
        'gs.content.form',
        'gs.viewlet',
        'Products.XWFChat',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
