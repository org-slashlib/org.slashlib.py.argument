# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   wrapper.py   is  distributed  WITHOUT ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for module 'org.slashlib.py.argument.parser.wrapper' """
from io             import StringIO
from typing         import Optional
from typing         import Union
from unittest       import TestCase
from unittest.mock  import patch

class Test_Module_wrapper( TestCase ):
    """ test module Test_Module_wrapper """

    def test_import_ArgumentParserWrapper( self ):
        """
            test if class 'ArgumentParserWrapper' can be imported from
            'org.slashlib.py.argument.parser.wrapper'
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper

    def test_static_getInstance_without_Arguments( self ):
        """
            test if 'ArgumentParserWrapper.getInstance'
            can be called without arguments.
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper
        parser = ArgumentParserWrapper.getInstance()

        self.assertIsNotNone( parser )
        self.assertTrue( isinstance( parser, ArgumentParserWrapper ))

    def test_static_register_without_Arguments_fails( self ):
        """
            test if 'ArgumentParserWrapper.register'
            can be called without arguments.
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper

        with self.assertRaises( TypeError ):
             ArgumentParserWrapper.register()

    def test_static_register_with_Argument_succeds_with_false_00( self ):
        """
            test if 'ArgumentParserWrapper.register' can be called
            with argument 'decorator' {None} and returns false
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper
        self.assertFalse( ArgumentParserWrapper.register( None ))

    def test_static_register_with_Argument_succeds_with_false_01( self ):
        """
            test if 'ArgumentParserWrapper.register' can be called
            with argument 'decorator' {dict} and returns false
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper
        self.assertFalse( ArgumentParserWrapper.register({ }));

    def test_static_register_with_Argument_succeds_with_true( self ):
        """
            test if 'ArgumentParserWrapper.register' can be called
            with argument 'decorator' {ArgumentParser} and returns true
        """
        from org.slashlib.py.argument.parser.wrapper            import ArgumentParserWrapper
        from org.slashlib.py.argument.typing.argument_decorator import ArgumentDecorator

        class Dummy( ArgumentDecorator ):
            def append( self, parser ):
                pass

        self.assertTrue( ArgumentParserWrapper.register( Dummy()));

    def test_static_reset_without_arguments_succeeds( self ):
        """
            test if 'ArgumentParserWrapper.reset' can be called without arguments.
        """
        from org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper
        ArgumentParserWrapper.reset()

    def test_ArgumentParserWrapper_parse_with_output_redicrection_00( self ):
        """
            test if 'ArgumentParserWrapper::parse' can be called.
            Arguments for redirecting output are passed to the function.
        """
        import sys
        from   org.slashlib.py.argument.parser.wrapper import ArgumentParserWrapper
        # make sure our new argument parser is not pulluted...
        ArgumentParserWrapper.reset()
        # prepare sys.argv
        oldargv  = sys.argv
        sys.argv = [ '<testarg:program>' ]

        stdout = StringIO()
        stderr = StringIO()

        try:
                 parser = ArgumentParserWrapper.getInstance()
                 parser.parse( stdout, stderr )

                 self.assertTrue( stdout.getvalue() == "" )
                 self.assertTrue( stderr.getvalue() == "" )
        finally:
                 sys.argv = oldargv
                 stdout.close()
                 stderr.close()

    def test_ArgumentParserWrapper_parse_with_output_redicrection_01( self ):
        """
            test if 'ArgumentParserWrapper::parse' can be called.
            Arguments for redirecting output are passed to the function.
        """
        import os
        import sys
        from   org.slashlib.py.argument                 import Argument
        from   org.slashlib.py.argument.parser.wrapper  import ArgumentParserWrapper
        # prepare sys.argv
        oldargv  = sys.argv
        filename = 'blubb'
        sys.argv = [ '<testarg:program>', '-f', filename ]

        stdout = StringIO()
        stderr = StringIO()

        try:
                 # make sure our new argument parser is not pulluted...
                 ArgumentParserWrapper.reset()

                 class MyClass:
                       @Argument
                       @property
                       def filename( self ) -> str:
                           "configuration filename"
                           pass

                 parser = ArgumentParserWrapper.getInstance( "Some Testing" )
                 parser.parse()

                 foo = MyClass()
                 self.assertTrue( foo.filename == filename )
        finally:
                 sys.argv = oldargv
                 stdout.close()
                 stderr.close()

    def test_ArgumentParserWrapper_parse_with_output_redicrection_02( self ):
        """
            test if 'ArgumentParserWrapper::parse' can be called.
            Arguments for redirecting output are passed to the function.
        """
        import os
        import sys
        from   org.slashlib.py.argument                 import Argument
        from   org.slashlib.py.argument.parser.wrapper  import ArgumentParserWrapper
        # prepare sys.argv
        oldargv  = sys.argv
        sys.argv = [ '<testarg:program>' ]

        stdout = StringIO()
        stderr = StringIO()

        try:
                 # make sure our new argument parser is not pulluted...
                 ArgumentParserWrapper.reset()

                 class MyClass:
                       @Argument( "dummy", default = "default blubb" )
                       @property
                       def filename( self ) -> str:
                           "configuration filename"
                           pass
                 with self.assertRaises( SystemExit ):
                      parser = ArgumentParserWrapper.getInstance( "Some Testing" )
                      parser.parse( outstream = stdout, errstream = stderr )

                 #print()
                 #print( "stdout: '%s'" % )
                 #print( "stderr: '%s'" % stderr.getvalue())

                 self.assertTrue( stdout.getvalue() == "" )
                 self.assertTrue( stderr.getvalue().startswith( "usage: Some Testing [-h] dummy\n" ))
        finally:
                 sys.argv = oldargv
                 stdout.close()
                 stderr.close()
