# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   package.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument.types' """
from enum           import Enum
from inspect        import isclass
from unittest       import TestCase

class Test_Package( TestCase ):
    """ test package 'org.slashlib.py.argument.types' """

    def test_import_Action( self ):
        """
            test if enumeration 'Action' can be imported from
            'org.slashlib.py.argument.types'
        """
        from org.slashlib.py.argument.types import Action
        self.assertIsNotNone( Action )
        self.assertTrue( isclass( Action ))
        self.assertTrue( issubclass( Action, Enum ))

    def test_import_NArgs( self ):
        """
            test if enumeration 'NArgs' can be imported from
            'org.slashlib.py.argument.types'
        """
        from org.slashlib.py.argument.types import NArgs
        self.assertIsNotNone( NArgs )
        self.assertTrue( isclass( NArgs ))
        self.assertTrue( issubclass( NArgs, Enum ))

    def test_import_NumberOfArguments( self ):
        """
            test if class 'NumberOfArguments' can be imported from
            'org.slashlib.py.argument.types'
        """
        from org.slashlib.py.argument.types import NumberOfArguments
        self.assertIsNotNone( NumberOfArguments )
        self.assertTrue( isclass( NumberOfArguments ))
