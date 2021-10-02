# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   package.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument.types' """
from enum           import Enum
from inspect        import isclass
from unittest       import TestCase

class Test_Package( TestCase ):
    """ test package 'org.slashlib.py.argument.types' """

    def test_import_ArgumentParser( self ):
        """
            test if class 'ArgumentParser' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import ArgumentParser
        self.assertIsNotNone( ArgumentParser )
        self.assertTrue( isclass( ArgumentParser ))

    def test_import_ConfigurationDecorator( self ):
        """
            test if class 'ConfigurationDecorator' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import ConfigurationDecorator
        self.assertIsNotNone( ConfigurationDecorator )
        self.assertTrue( isclass( ConfigurationDecorator ))

    def test_import_PropertyDecorator( self ):
        """
            test if class 'PropertyDecorator' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import PropertyDecorator
        self.assertIsNotNone( PropertyDecorator )
        self.assertTrue( isclass( PropertyDecorator ))

    def test_import_ArgumentDecorator( self ):
        """
            test if class 'ArgumentDecorator' can be imported from
            'org.slashlib.py.argument.typing'
        """
        from org.slashlib.py.argument.typing import ArgumentDecorator
        self.assertIsNotNone( ArgumentDecorator )
        self.assertTrue( isclass( ArgumentDecorator ))
