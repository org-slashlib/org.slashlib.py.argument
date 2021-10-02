# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_decorator.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty  of MERCHANTABILITY  or FITNESS FOR  A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.typing.argument_decorator' """
from inspect        import isclass
from inspect        import isfunction
from typing         import Protocol
from unittest       import TestCase

class Test_Module_argument_decorator( TestCase ):
    """ test module argument_decorator """

    def test_import_ArgumentDecorator( self ):
        """
            test if class 'ArgumentDecorator' can be imported from
            'org.slashlib.py.argument.typing.argument_decorator'
        """
        from org.slashlib.py.argument.typing.argument_decorator import ArgumentDecorator
        self.assertIsNotNone( ArgumentDecorator )
        self.assertTrue( isclass( ArgumentDecorator ))
        self.assertTrue( issubclass( ArgumentDecorator, Protocol ))

    def test_ArgumentDecorator_new_failure( self ):
        """
            make sure, creating instances of abstract class
            'ArgumentDecorator' fails.
        """
        from org.slashlib.py.argument.typing.argument_decorator import ArgumentDecorator

        with self.assertRaises( TypeError ) as context:
             argdec = ArgumentDecorator()

        errmsg = "Can't instantiate abstract class ArgumentDecorator"
        self.assertTrue( str( context.exception ).startswith( errmsg ))

    def test_ArgumentDecorator_append( self ):
        """
            make sure, protocol 'ArgumentDecorator' declares method
            'append'.
        """
        from org.slashlib.py.argument.typing.argument_decorator import ArgumentDecorator

        self.assertIsNotNone( ArgumentDecorator.append )
        self.assertTrue( isfunction( ArgumentDecorator.append ))
