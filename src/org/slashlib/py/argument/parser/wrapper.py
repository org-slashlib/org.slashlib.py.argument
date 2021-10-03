# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   wrapper.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
"""  """
import sys

from   abc                              import ABCMeta
from   argparse                         import ArgumentParser as ArgParse
from   argparse                         import Namespace      as ArgParseNamespace
from   typing                           import Any
from   typing                           import Dict
from   typing                           import Final
from   typing                           import List
from   typing                           import Optional
from   typing                           import TextIO

from   org.slashlib.py.argument.typing      import ArgumentDecorator
from   org.slashlib.py.argument.typing      import ArgumentParser

# provide an empty list for adding @Argument(s)
ARGUMENTDECORATORS: Final[ List[ ArgumentDecorator ]] = list()
ARGUMENTPARSER: Optional[ ArgumentParser ] = None

class ArgumentParserWrapper( ArgumentParser, metaclass = ABCMeta ):
    """
        Class ArgumentParserWrapper is a singleton. Call static method
        <code>ArgumentParserWrapper.getInstance( ... )</code> to get
        access to an instance of class ArgumentParserWrapper.
    """
    @staticmethod
    def getInstance( prog:   str = None, usage: str = None, description: str = None,
                     epilog: str = None ) -> ArgumentParser:
        """
            Returns a singleton, which wraps 'ArgumentParser'
            from pythons package 'argparse'.
        """
        if  ( ARGUMENTPARSER is None ):
              class AnonArgumentParserWrapper( ArgumentParserWrapper ):
                    def __init__( self, prog, usage, description, epilog ):
                        super().__init__( prog, usage, description, epilog )
                        ARGUMENTPARSER = self

              return AnonArgumentParserWrapper( prog, usage, description, epilog )
        else: return ARGUMENTPARSER

    @staticmethod
    def register( decorator: ArgumentDecorator ) -> bool:
        """
            Register an @Argument with an ArgumentParser.
        """
        if (( not ( decorator is None )) and
            ( isinstance( decorator, ArgumentDecorator ))):
              if  ( ARGUMENTPARSER is None ):
                    ARGUMENTDECORATORS.append( decorator )
              else: decorator.append( ARGUMENTPARSER )
              return True
        else: return False

    @staticmethod
    def reset():
        """
            Implemented for testing purposes. Usually this feature should not be
            required.
            It can be used to reset (clear) ARGUMENTDECORATORS and ARGUMENTPASER.
        """
        ARGUMENTDECORATORS.clear()
        ARGUMENTPARSER = None

    def __init__( self, prog: str        = None, usage: str    = None,
                        description: str = None, epilog: str   = None ) -> None:
        """
            Create an ArgumentParserWrapper.
        """
        # cache parsed arguments ... initially None
        self._arguments: Optional[ ArgParseNamespace ] = None

        # prepare pythons argument parser
        self._parser = ArgParse( prog        = prog,        usage = usage,
                                 description = description,
                                 epilog      = epilog )

        # prepare named mutual exclusive groups for grouping arguments
        self._groups: Dict[ str, Any ] = dict()

        # trigger arguments from list to append themselves
        for argument in ARGUMENTDECORATORS:
            argument.append( self )

        # clear the list of argument decorators after decorators have been
        # appended to the argument parser
        ARGUMENTDECORATORS.clear()

    def addArgument( self, *nameorflags: str, **kwargs ):
        """
            Add an argument to the ArgumentParser.
        """
        self._parser.add_argument( *nameorflags, **kwargs )

    def addGroupedArgument( self, groupname: str, *nameorflags: str, **kwargs ):
        """
            Add an argument to a named mutual exclusive group.
        """
        if  ( groupname is None ):
              raise TypeError( "ArgumentParserWrapper.addGroupedArgument: Parameter 'groupname' must be of type 'str'" )
        else: pass

        if  ( not ( groupname in self._groups )):
              self._groups[ groupname ] = self._parser.add_mutually_exclusive_group()
        else: pass

        self._groups[ groupname ].add_argument( *nameorflags, **kwargs )

    def parse( self, arguments: str    = None,  outstream: TextIO = sys.stdout,
                     errstream: TextIO = sys.stderr ) -> ArgParseNamespace:
        """
            Parse arguments passed to the script/program
        """
        if  ( self._arguments is None ):
              oldstdout  = sys.stdout
              oldstderr  = sys.stderr
              sys.stdout = outstream
              sys.stderr = errstream

              try:     self._arguments = self._parser.parse_args( arguments )
              finally:
                       sys.stdout = oldstdout
                       sys.stderr = oldstderr
        else: pass

        return self._arguments
