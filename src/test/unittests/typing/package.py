# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   package.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument.typing' """
from inspect        import isclass
from unittest       import TestCase

class Test_Package( TestCase ):
    """ test package 'org.slashlib.py.argument.types' """

    def test_import_ArgumentDecorator( self ):
        """
            test if class 'ArgumentDecorator' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import ArgumentDecorator
        self.assertIsNotNone( ArgumentDecorator )
        self.assertTrue( isclass( ArgumentDecorator ))

    def test_import_ArgumentParser( self ):
        """
            test if class 'ArgumentParser' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import ArgumentParser
        self.assertIsNotNone( ArgumentParser )
        self.assertTrue( isclass( ArgumentParser ))
