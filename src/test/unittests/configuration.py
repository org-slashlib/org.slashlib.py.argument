# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   configuration.py  is distributed  WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument.configuration' """
from typing         import Optional
from typing         import Union
from unittest       import TestCase

class Test_Module_configuration( TestCase ):
    """ test module Test_Module_configuration """

    def test_import_Configuration( self ):
        """
            test if class 'Configuration' can be imported from
            'org.slashlib.py.argument.configuration'
        """
        from org.slashlib.py.argument.configuration import Configuration

    def test_Configuration_new_without_arguments( self ):
        """
            test if class 'Configuration' can be created
        """
        from org.slashlib.py.argument.configuration import Configuration

        cfg = Configuration()

    def test_Configuration_new_with_arguments( self ):
        """
            test if class 'Configuration' can be created
        """
        from org.slashlib.py.argument.configuration import Configuration

        cfg = Configuration( name = "default" )

    def test_Configuration_new_with_template_class_01( self ):
        """
            test if class 'Configuration' can be created
        """
        from org.slashlib.py.argument.configuration import Configuration
        class Default:
            pass
        cfg = Configuration( Default )

    def test_Configuration_new_with_template_class_02( self ):
        """
            test if class 'Configuration' can be created
        """
        from org.slashlib.py.argument.configuration import Configuration

        @Configuration
        class Default:
            def __init__( self, test ):
                pass

        dflt = Default( "fun1" )

    def test_Configuration_new_with_template_class_03( self ):
        """
            test if class 'Configuration' can be created
        """
        from org.slashlib.py.argument.configuration import Configuration

        @Configuration( name = "foo", desc = "bar" )
        class Default:
            def __init__( self, test ):
                pass

        dflt = Default( "fun2" )
