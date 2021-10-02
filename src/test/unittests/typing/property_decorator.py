# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   property_decorator.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty  of MERCHANTABILITY  or FITNESS FOR  A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.typing.property_decorator' """
from inspect        import isabstract
from inspect        import isclass
from inspect        import isfunction
from typing         import Protocol
from unittest       import TestCase

class Test_Module_property_decorator( TestCase ):
    """ test module property_decorator """

    def test_import_PropertyDecorator( self ):
        """
            test if class 'PropertyDecorator' can be imported from
            'org.slashlib.py.argument.typing.property_decorator'
        """
        from org.slashlib.py.argument.typing.property_decorator import PropertyDecorator
        self.assertIsNotNone( PropertyDecorator )
        self.assertTrue( isclass( PropertyDecorator ))
        # self.assertTrue( isabstract( PropertyDecorator ))

    #def test_PropertyDecorator_new_failure( self ):
        #"""
        #    make sure, creating instances of abstract class
        #    'PropertyDecorator' fails.
        #"""
        # note: this does not work for abstract classes without abstract methods...
        #from org.slashlib.py.argument.typing.property_decorator import PropertyDecorator

        #with self.assertRaises( TypeError ) as context:
        #argdec = PropertyDecorator()

        #errmsg = "Can't instantiate abstract class PropertyDecorator"
        #self.assertTrue( str( context.exception ).startswith( errmsg ))
