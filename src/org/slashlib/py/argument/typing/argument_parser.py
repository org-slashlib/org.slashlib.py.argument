# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_parser.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR  A PARTICULAR PURPOSE.
#
import sys
from   abc          import abstractmethod
from   argparse     import Namespace      as ArgParseNamespace
from   typing       import Any
from   typing       import Protocol
from   typing       import TextIO
from   typing       import runtime_checkable

class ArgumentParser( Protocol ):
    """
        Protocol for ArgumentParser(s). Required for compatiblility with
        'org.slashlib.py.argument'.

        - add an argument:
          addArgument( *nameorflags: str, **kwargs ):

        - add an argument to a named mutual exclusive group
          addGroupedArgument( groupname: str, *nameorflags: str, **kwargs ):

        - trigger argument parsing
          parse( self, outstream: TextIO, errstream: TextIO ) -> Any:

    """
    @abstractmethod
    def addArgument( self, *nameorflags: str, **kwargs ):
        """
            Add an argument to the ArgumentParser.
        """
        raise NotImplementedError

    @abstractmethod
    def addGroupedArgument( self, groupname: str, *nameorflags: str, **kwargs ):
        """
            Add an argument to a named mutual exclusive group.

            Args:
                groupname:      Name of mutual excluseive group.
                nameorflags:    List of argument names and flags.
                kwargs:         @Argument properties.
        """
        raise NotImplementedError

    @abstractmethod
    def parse( self, arguments: str    = None,  outstream: TextIO = sys.stdout,
                     errstream: TextIO = sys.stderr ) -> ArgParseNamespace:
        """
            Parse arguments passed to the script/program
        """
        raise NotImplementedError
