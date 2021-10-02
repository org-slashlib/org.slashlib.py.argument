# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument.py  is  distributed  WITHOUT ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument' """
from typing         import Optional
from typing         import Union
from unittest       import TestCase

class Test_Module_argument( TestCase ):
    """ test module Test_Module_argument """

    def test_import_Argument( self ):
        """
            test if class 'Argument' can be imported from
            'org.slashlib.py.argument.argument'
        """
        from org.slashlib.py.argument.argument import Argument

    def test_Argument_new_success( self ):
        """
            Ensure '@Argument' can be created without any arguments
        """
        from org.slashlib.py.argument.argument import Argument
        argument = Argument()
        self.assertIsNotNone( argument )
        self.assertTrue( isinstance( argument, Argument ))

    def test_Argument_on_property_success_00_00( self ):
        """
            Ensure '@Argument' can be created with property as argument.
        """
        from org.slashlib.py.argument.argument import Argument

        returnvalue = "value"

        class Fun:
            def __init__( self ):
                self._foo = returnvalue

            @Argument
            @property
            def foo( self ) -> str:
                """example propertty foo"""
                return self._foo

        f = Fun()

        self.assertIsNotNone( f.foo )
        self.assertTrue( returnvalue == f.foo )

    def test_Argument_on_property_success_00_01( self ):
        """
            Ensure '@Argument' can be created with property as argument.
            Ensure property setter works.
        """
        from org.slashlib.py.argument.argument import Argument

        returnvalue = "value"
        newvalue    = "newvalue"

        class Fun:
            def __init__( self ):
                self._foo = returnvalue

            @Argument
            @property
            def foo( self ) -> str:
                """example propertty foo"""
                return self._foo

            @foo.setter
            def foo( self, value ):
                """setter for property foo"""
                self._foo = value

        f = Fun()

        self.assertIsNotNone( f.foo )
        self.assertTrue( returnvalue == f.foo )

        f.foo = newvalue
        self.assertIsNotNone( f.foo )
        self.assertTrue( newvalue == f.foo )

    def test_Argument_on_property_success_01_00( self ):
        """
            Ensure '@Argument' can be created with arguments and property.
        """
        from org.slashlib.py.argument.argument import Argument

        returnvalue  = "returnvalue"

        class Fun:
            def __init__( self ):
                self._foo = returnvalue

            @Argument( "f", "fun" )
            @property
            def foo( self ) -> str:
                """example propertty foo"""
                return self._foo

        f = Fun()

        self.assertIsNotNone( f.foo )
        self.assertTrue( returnvalue == f.foo )

    def test_Argument_on_property_success_01_01( self ):
        """
            Ensure '@Argument' can be created with arguments and property.
            Ensure property setter works.
        """
        from org.slashlib.py.argument.argument import Argument

        returnvalue = "returnvalue"
        newvalue    = "newvalue"

        class Fun:
            def __init__( self ):
                self._foo = returnvalue

            @Argument( "f", "fun" )
            @property
            def foo( self ) -> str:
                """example propertty foo"""
                return self._foo

            @foo.setter
            def foo( self, value ):
                """setter for property foo"""
                self._foo = value

        f = Fun()

        self.assertIsNotNone( f.foo )
        self.assertTrue( returnvalue == f.foo )

        f.foo = newvalue
        self.assertIsNotNone( f.foo )
        self.assertTrue( newvalue == f.foo )

    def test_Argument_on_function_fail_01( self ):
        """
            make sure '@Argument' cannot be created with function as argument.
        """
        from org.slashlib.py.argument.argument import Argument

        with self.assertRaises( TypeError ):
             @Argument
             def foo():
                 pass

    def test_Argument_on_function_fail_02( self ):
        """
            make sure '@Argument' cannot be created with arguments and function.
        """
        from org.slashlib.py.argument.argument import Argument

        with self.assertRaises( TypeError ):
             @Argument()
             def foo():
                 pass
