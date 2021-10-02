#!/usr/bin/env python
#
#   © 2009, slashlib.org.
#
#   setup.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A PARTICULAR  PURPOSE.
#
from setuptools import setup, find_packages
import os

filemode    = "rb"
filecmd     = "exec"
localfile   = os.path.join( "src", "org", "slashlib", "py", "argument", 'version.py' )
exec( compile( open( localfile, filemode ).read(), localfile, filecmd ))

setup(
    name                = PROJECTNAMESPACE,
    version             = VERSION,
    description         = LONGDESCRIPTION,
    author              = AUTHOR,
    author_email        = EMAIL,
    url                 = WEBSITE,
    packages            = find_packages( SRC, exclude = [ "test", "test.*" ]),
    package_dir         = { "" : SRC },
    namespace_packages  = NAMESPACES,
    classifiers         = [
                            "Development Status :: 1 - Alpha",
                            "Environment :: Console",
                            "Intended Audience :: Developers",
                            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
                            "Natural Language :: English",
                            "Natural Language :: German",
                            "Operating System :: OS Independent",
                            "Programming Language :: Python",
                            "Programming Language :: Python :: 3.9",
                            "Framework :: org.slashlib.py ",
                            "Framework :: org.slashlib.py :: argument",
                            "Topic :: Software Development :: Libraries :: Python Modules",
                            "Topic :: Command-line argument parsing"
                          ],
    license             = LICENSE,
    package_data        = {
                            "org.slashlib.py.argument":         [ "py.typed" ],
                            "org.slashlib.py.argument.parser":  [ "py.typed" ],
                            "org.slashlib.py.argument.types":   [ "py.typed" ],
                            "org.slashlib.py.argument.typing":  [ "py.typed" ]
                          },
    install_requires    = [ ],
    extras_require      = { },
    zip_safe            = False,
)
