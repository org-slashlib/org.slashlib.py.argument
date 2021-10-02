# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_parser.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.typing.argument_parser' """
from inspect        import isclass
from inspect        import isfunction
from typing         import Protocol
from unittest       import TestCase

class Test_Module_argument_parser( TestCase ):
    """ test module argument_parser """

    def test_import_ArgumentParser( self ):
        """
            test if class 'ArgumentParser' can be imported from
            'org.slashlib.py.argument.typing.argument_parser'
        """
        from org.slashlib.py.argument.typing.argument_parser import ArgumentParser
        self.assertIsNotNone( ArgumentParser )
        self.assertTrue( isclass( ArgumentParser ))
        self.assertTrue( issubclass( ArgumentParser, Protocol ))

    def test_ArgumentParser_new_failure( self ):
        """
            make sure, creating instances of abstract class
            'ArgumentParser' fails.
        """
        from org.slashlib.py.argument.typing.argument_parser import ArgumentParser

        with self.assertRaises( TypeError ) as context:
             argpars = ArgumentParser()

        errmsg = "Can't instantiate abstract class ArgumentParser"
        self.assertTrue( str( context.exception ).startswith( errmsg ))

    def test_ArgumentParser_addArgument( self ):
        """
            make sure, protocol 'ArgumentParser' declares method
            'addArgument'.
        """
        from org.slashlib.py.argument.typing.argument_parser import ArgumentParser

        self.assertIsNotNone( ArgumentParser.addArgument )
        self.assertTrue( isfunction( ArgumentParser.addArgument ))

        with self.assertRaises( NotImplementedError ) as context:
             ArgumentParser.addArgument( None )

    def test_ArgumentParser_addGroupedArgument( self ):
        """
            make sure, protocol 'ArgumentParser' declares method
            'addGroupedArgument'.
        """
        from org.slashlib.py.argument.typing.argument_parser import ArgumentParser

        self.assertIsNotNone( ArgumentParser.addGroupedArgument )
        self.assertTrue( isfunction( ArgumentParser.addGroupedArgument ))

        with self.assertRaises( NotImplementedError ) as context:
             ArgumentParser.addGroupedArgument( None, None )

    def test_ArgumentParser_parse( self ):
        """
            make sure, protocol 'ArgumentParser' declares method
            'parse'.
        """
        from org.slashlib.py.argument.typing.argument_parser import ArgumentParser

        self.assertIsNotNone( ArgumentParser.parse )
        self.assertTrue( isfunction( ArgumentParser.parse ))

        with self.assertRaises( NotImplementedError ) as context:
             ArgumentParser.parse( None, None, None )
