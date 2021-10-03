# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   nargs.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty of  MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.
#
from typing                             import Type
from typing                             import Union

class NumberOfArguments:
    @property
    def type( self ) -> Union[ Type[ int ], Type[ int ]]:
        return self._type

    @property
    def optional( self ) -> bool:
        return self._optional

    @property
    def name( self ) -> str:
        return self._name_

    @property
    def value( self ) -> Union[ str, int ]:
        if  ( not ( self._count_ is None )):
              return self._count_
        else: return self._value_
