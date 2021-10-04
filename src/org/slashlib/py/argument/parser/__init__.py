# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   __init__.py  is distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" parser required by org.slashlib.py.argument """

from typing                         import Optional
from typing                         import TextIO

from org.slashlib.py.argument.typing    import ArgumentDecorator
from org.slashlib.py.argument.typing    import ArgumentParser

from .wrapper                       import ArgumentParserWrapper

def getInstance( *args, **kwargs ) -> ArgumentParser:
    """
        Returns an ArgumentParser singleton, which wraps
        'ArgumentParser' from pythons package 'argparse'.

        Note:   This is not part of the public interface
                of package 'org.slashlib.py.argument',
                because it should only be called by
                @Configuration.
    """
    return ArgumentParserWrapper.getInstance( *args, **kwargs )

def register( decorator: ArgumentDecorator ) -> bool:
    """
        Register an @Argument with an ArgumentParser.
    """
    return ArgumentParserWrapper.register( decorator )

def requestInstance() -> ArgumentParser:
    """
        Request an [existing] instance of type ArgumentParser.
        Raise ReferenceError, if not available.
    """
    return ArgumentParserWrapper.requestInstance()

def reset() -> None:
    """
        Implemented for testing purposes.
    """
    return ArgumentParserWrapper.reset()
