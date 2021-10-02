# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   configuration_decorator.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty  of MERCHANTABILITY  or FITNESS FOR  A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.typing.configuration_decorator' """
from inspect        import isclass
from inspect        import isfunction
from typing         import Protocol
from unittest       import TestCase

class Test_Module_configuration_decorator( TestCase ):
    """ test module configuration_decorator """

    def test_import_ConfigurationDecorator( self ):
        """
            test if class 'ConfigurationDecorator' can be imported from
            'org.slashlib.py.argument.typing.configuration_decorator'
        """
        from org.slashlib.py.argument.typing.configuration_decorator import ConfigurationDecorator
        self.assertIsNotNone( ConfigurationDecorator )
        self.assertTrue( isclass( ConfigurationDecorator ))
        self.assertTrue( issubclass( ConfigurationDecorator, Protocol ))

    def test_ConfigurationDecorator_new_failure( self ):
        """
            make sure, creating instances of abstract class
            'ConfigurationDecorator' fails.
        """
        from org.slashlib.py.argument.typing.configuration_decorator import ConfigurationDecorator

        with self.assertRaises( TypeError ) as context:
             argdec = ConfigurationDecorator()

        errmsg = "Protocols cannot be instantiated"
        self.assertTrue( str( context.exception ).startswith( errmsg ))
