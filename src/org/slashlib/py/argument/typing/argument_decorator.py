# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_decorator.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty of  MERCHANTABILITY or  FITNESS FOR  A PARTICULAR PURPOSE.
#
from abc                                import abstractmethod
from typing                             import Protocol
from typing                             import runtime_checkable

from org.slashlib.py.argument.typing    import ArgumentParser

@runtime_checkable
class ArgumentDecorator( Protocol ):
      @abstractmethod
      def append( self, parser: ArgumentParser ):
          """
              Triggers an @Argument to append itself to 'parser'

              Args:
                parser:     A parser for script/program arguments.

              Raises:
                NotImplementedError:    If super().append( ... ) accidentally
                                        calls abstract method append of protocol
                                        ArgumentDecorator.
          """
          raise NotImplementedError
