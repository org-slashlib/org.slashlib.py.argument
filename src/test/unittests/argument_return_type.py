# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_return_type.py  is distributed  WITHOUT ANY WARRANTY;  without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument' """
from unittest                           import TestCase
from typing                             import Optional

class Test_Module_argument_return_type( TestCase ):
    """ test module Test_Module_argument_return_type """

    def test_Argument_simple_mandatory_return_type( self ):
        """
            Ensure '@Argument' reads return type from getter.
        """
        from org.slashlib.py.argument.argument import Argument

        class Fun:
            def __init__( self ):
                self._foo = "returnvalue"

            @Argument
            @property
            def foo( self ) -> str:
                """example propertty foo"""
                return self._foo

    def test_Argument_simple_mandatory_return_type_mismatch( self ):
        """
            Ensure '@Argument' fails, if arguments and return type
            from getter are ambiguous.
        """
        from org.slashlib.py.argument.argument import Argument

        with self.assertRaises( TypeError ):
             class Fun:
                 def __init__( self ):
                     self._foo = "returnvalue"

                 @Argument( type = "int" )
                 @property
                 def foo( self ) -> str:
                     """example propertty foo"""
                     return self._foo

    def test_Argument_simple_optional_return_type( self ):
        """
            Ensure '@Argument' reads optional return type from getter.
        """
        from org.slashlib.py.argument.argument import Argument

        class Fun:
            def __init__( self ):
                self._foo = "returnvalue"

            @Argument
            @property
            def foo( self ) -> Optional[ str ]:
                """example propertty foo"""
                return self._foo

    def test_Argument_simple_optional_return_type_mismatch( self ):
        """
            Ensure '@Argument' fails, if arguments and return type
            from getter are ambiguous.
        """
        from org.slashlib.py.argument.argument import Argument

        with self.assertRaises( TypeError ):
             class Fun:
                 def __init__( self ):
                     self._foo = "returnvalue"

                 @Argument( type = "bool" )
                 @property
                 def foo( self ) -> Optional[ str ]:
                     """example propertty foo"""
                     return self._foo

    def test_Argument_simple_optional_return_type_mismatch( self ):
        """
            Ensure '@Argument' fails, if arguments and return type
            from getter are ambiguous.
        """
        from org.slashlib.py.argument.argument import Argument

        #with self.assertRaises( TypeError ):
        class Fun:
             def __init__( self ):
                 self._foo = "returnvalue"

             @Argument( nargs = "?" )
             @property
             def foo( self ) -> Optional[ str ]:
                 """example propertty foo"""
                 return self._foo
