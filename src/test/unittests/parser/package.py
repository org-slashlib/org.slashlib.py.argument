# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   package.py   is  distributed  WITHOUT ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.argument.parser' """
from unittest       import TestCase

class Test_Package( TestCase ):
    def test_import_package( self ):
        """
            test if package 'org.slashlib.py.argument.parser' can be imported.
        """
        import org.slashlib.py.argument.parser

    def test_import_package_getInstance( self ):
        """
            test if function 'getInstance' can be imported
            from package 'org.slashlib.py.argument.parser'
        """
        from org.slashlib.py.argument.parser    import getInstance
        self.assertIsNotNone( getInstance )
        self.assertTrue( callable( getInstance ))

    def test_import_package_register( self ):
        """
            test if function 'register' can be imported
            from package 'org.slashlib.py.argument.parser'
        """
        from org.slashlib.py.argument.parser    import register
        self.assertIsNotNone( register )
        self.assertTrue( callable( register ))

    def test_import_package_reset( self ):
        """
            test if function 'reset' can be imported
            from package 'org.slashlib.py.argument.parser'
        """
        from org.slashlib.py.argument.parser    import reset
        self.assertIsNotNone( reset )
        self.assertTrue( callable( reset ))
