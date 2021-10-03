# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   package.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument' """
from inspect        import isclass
from unittest       import TestCase

class Test_Package( TestCase ):
    """ test package 'org.slashlib.py.argument.types' """

    def test_import_Argument( self ):
        """
            test if class 'Argument' can be imported from
            'org.slashlib.py.argument'
        """
        from org.slashlib.py.argument import Argument
        self.assertIsNotNone( Argument )
        self.assertTrue( isclass( Argument ))
