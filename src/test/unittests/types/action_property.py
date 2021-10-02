# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   action_property.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY  or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.types.action_property' """
from inspect        import isclass
from unittest       import TestCase

class Test_Module_action_property( TestCase ):
    """ test module action_property """

    def test_import_ActionProperty( self ):
        """
            test if class 'ActionProperty' can be imported from
            'org.slashlib.py.argument.types.action_property'
        """
        from org.slashlib.py.argument.types.action_property import ActionProperty
        self.assertIsNotNone( ActionProperty )
        self.assertTrue( isclass( ActionProperty ))
        self.assertTrue( issubclass( ActionProperty, property ))

    def test_ActionProperty_from_failure_01( self ):
        """
            test staticmethod 'ActionProperty.from()' without arguments
        """
        from org.slashlib.py.argument.types.action_property import ActionProperty

        with self.assertRaises( TypeError ):
             # TypeError: fromProperty() missing 2 required positional
             #            arguments: 'prop' and 'decorator'
             ActionProperty.fromProperty( )

    def test_ActionProperty_from_failure_02( self ):
        """
            test staticmethod 'ActionProperty.from()' with arguments of wrong type
        """
        from org.slashlib.py.argument.types.action_property import ActionProperty

        with self.assertRaises( TypeError ):
             # TypeError: ActionProperty.fromProperty: Parameter 'prop' must be
             #            of type 'property'
             ActionProperty.fromProperty( "wrong type", "wrong type" )

    def test_ActionProperty_from_failure_03( self ):
        """
            test staticmethod 'ActionProperty.from()' with second argument of wrong type
        """
        from org.slashlib.py.argument.types.action_property import ActionProperty

        with self.assertRaises( TypeError ):
             # TypeError: ActionProperty.decorator[setter]: Parameter 'decorator'
             #            must be of type 'PropertyDecorator'
             def actionproperty( prop ):
                 return ActionProperty.fromProperty( prop, "wrong type" )

             class Bar():
                 @actionproperty
                 @property
                 def value( self ):
                     return self._value

                 @value.setter
                 def value( self, value ):
                     self._value

    def test_ActionProperty_from_success( self ):
        """
            test staticmethod 'ActionProperty.from()' and make sure
            actionproperty.setter( ... ) is called.
        """
        from org.slashlib.py.argument.types.action_property import ActionProperty
        from org.slashlib.py.argument.types.action_property import PropertyDecorator

        oldsetter = ActionProperty.setter
        testinst  = self

        def action_property_setter( self, fset ):
            testinst.assertIsNotNone( fset )
            return oldsetter( self, fset )

        ActionProperty.setter = action_property_setter

        class Foo( PropertyDecorator ):
            pass

        def actionproperty( prop ):
            foo = Foo()
            return ActionProperty.fromProperty( prop, foo )

        class Bar():
            @actionproperty
            @property
            def value( self ):
                return self._value

            @value.setter
            def value( self, value ):
                self._value
