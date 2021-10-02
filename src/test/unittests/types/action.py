# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   action.py   is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.types.action' """
from enum           import Enum
from inspect        import isclass
from unittest       import TestCase

class Test_Module_action( TestCase ):
    """ test module action """

    def test_import_Action( self ):
        """
            test if enumeration 'Action' can be imported from
            'org.slashlib.py.argument.types.action'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action )
        self.assertTrue( isclass( Action ))
        self.assertTrue( issubclass( Action, Enum ))

    def test_Action_for_Append( self ):
        """
            test if enumeration 'Action' provides 'Append'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Append )
        self.assertTrue( isinstance( Action.Append, Action ))

    def test_Action_for_AppendConst( self ):
        """
            test if enumeration 'Action' provides 'AppendConst'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.AppendConst )
        self.assertTrue( isinstance( Action.AppendConst, Action ))

    def test_Action_for_Count( self ):
        """
            test if enumeration 'Action' provides 'Count'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Count )
        self.assertTrue( isinstance( Action.Count, Action ))

    def test_Action_for_Extend( self ):
        """
            test if enumeration 'Action' provides 'Extend'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Extend )
        self.assertTrue( isinstance( Action.Extend, Action ))

    def test_Action_for_Help( self ):
        """
            test if enumeration 'Action' provides 'Help'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Help )
        self.assertTrue( isinstance( Action.Help, Action ))

    def test_Action_for_Store( self ):
        """
            test if enumeration 'Action' provides 'Store'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Store )
        self.assertTrue( isinstance( Action.Store, Action ))

    def test_Action_for_StoreConst( self ):
        """
            test if enumeration 'Action' provides 'StoreConst'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.StoreConst )
        self.assertTrue( isinstance( Action.StoreConst, Action ))

    def test_Action_for_StoreFalse( self ):
        """
            test if enumeration 'Action' provides 'StoreFalse'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.StoreFalse )
        self.assertTrue( isinstance( Action.StoreFalse, Action ))

    def test_Action_for_StoreTrue( self ):
        """
            test if enumeration 'Action' provides 'StoreTrue'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.StoreTrue )
        self.assertTrue( isinstance( Action.StoreTrue, Action ))

    def test_Action_for_Version( self ):
        """
            test if enumeration 'Action' provides 'Version'
        """
        from org.slashlib.py.argument.types.action import Action
        self.assertIsNotNone( Action.Version )
        self.assertTrue( isinstance( Action.Version, Action ))

    def test_Action_from_str_failure_01( self ):
        """
            test 'Action' enumerations static method 'from_str'
        """
        from org.slashlib.py.argument.types.action import Action
        dummy = Action.from_str( "vAlUe" )
        self.assertIsNone( dummy )


    def test_Action_from_str_success_01( self ):
        """
            test 'Action' enumerations static method 'from_str'
        """
        from org.slashlib.py.argument.types.action import Action
        dummy = Action.from_str( "vErSiOn" )
        self.assertIsNotNone( dummy )
        self.assertTrue( dummy is Action.Version )

    def test_Action_to_str( self ):
        """
            test 'Action' enumerations string conversion
        """
        from org.slashlib.py.argument.types.action import Action
        strval = str( Action.Version )
        self.assertIsNotNone( strval )
        self.assertTrue( strval == Action.Version.value )
