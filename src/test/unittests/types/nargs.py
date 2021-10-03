# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   NArgs.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A PARTICULAR  PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.types.NArgs' """
from enum           import Enum
from inspect        import isclass
from unittest       import TestCase

class Test_Module_NArgs( TestCase ):
    """ test module NArgs """

    def test_import_NArgs( self ):
        """
            test if enumeration 'NArgs' can be imported from
            'org.slashlib.py.argument.types.NArgs'
        """
        from org.slashlib.py.argument.types.nargs import NArgs
        self.assertIsNotNone( NArgs )
        self.assertTrue( isclass( NArgs ))
        self.assertTrue( issubclass( NArgs, Enum ))

    def test_NArgs_for_SetOf( self ):
        """
            test if enumeration 'NArgs' provides 'SetOf'
        """
        from org.slashlib.py.argument.types.nargs import NArgs
        self.assertIsNotNone( NArgs.SetOf )
        self.assertTrue( isinstance( NArgs.SetOf, NArgs ))
        self.assertTrue( NArgs.SetOf.name == "SetOf" )
        self.assertTrue( NArgs.SetOf.value == None )
        self.assertTrue( NArgs.SetOf.optional == False )
        self.assertTrue( NArgs.SetOf.type == type( int ))

    def test_NArgs_for_OneOptional( self ):
        """
            test if enumeration 'NArgs' provides 'OneOptional'
        """
        from org.slashlib.py.argument.types.nargs import NArgs
        self.assertIsNotNone( NArgs.OneOptional )
        self.assertTrue( isinstance( NArgs.OneOptional, NArgs ))
        self.assertTrue( NArgs.OneOptional.name == "OneOptional" )
        self.assertTrue( NArgs.OneOptional.value == "?" )
        self.assertTrue( NArgs.OneOptional.optional == True )
        self.assertTrue( NArgs.OneOptional.type == type( int ))

    def test_NArgs_for_Many( self ):
        """
            test if enumeration 'NArgs' provides 'Many'
        """
        from org.slashlib.py.argument.types.nargs import NArgs
        self.assertIsNotNone( NArgs.Many )
        self.assertTrue( isinstance( NArgs.Many, NArgs ))
        self.assertTrue( NArgs.Many.name == "Many" )
        self.assertTrue( NArgs.Many.value == "+" )
        self.assertTrue( NArgs.Many.optional == False )
        self.assertTrue( NArgs.Many.type == type( int ))

    def test_NArgs_for_ManyOptional( self ):
        """
            test if enumeration 'NArgs' provides 'ManyOptional'
        """
        from org.slashlib.py.argument.types.nargs import NArgs
        self.assertIsNotNone( NArgs.ManyOptional )
        self.assertTrue( isinstance( NArgs.ManyOptional, NArgs ))
        self.assertTrue( NArgs.ManyOptional.name == "ManyOptional" )
        self.assertTrue( NArgs.ManyOptional.value == "*" )
        self.assertTrue( NArgs.ManyOptional.optional == True )
        self.assertTrue( NArgs.ManyOptional.type == type( int ))

    def test_NArgs_parse_int( self ):
        from org.slashlib.py.argument.types.nargs import NArgs
        value = 6
        enumeration = NArgs.parse( value )
        self.assertIsNotNone( enumeration )
        # self.assertTrue( isinstance( enumeration, NArgs ))
        self.assertTrue( enumeration.name == NArgs.ManyOptional.SetOf.name )
        self.assertTrue( enumeration.value == value )
        self.assertTrue( enumeration.optional == False )
        self.assertTrue( enumeration.type == type( int ))
