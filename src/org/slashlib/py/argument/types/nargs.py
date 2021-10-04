# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   nargs.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty of  MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.
#
from enum                       import Enum
from typing                     import cast
from typing                     import Optional
from typing                     import Type
from typing                     import Union
from typing                     import Final
from .numberofarguments         import NumberOfArguments

class CArgs( NumberOfArguments ):
    def __init__( self, count: int ) -> None:
        self._value_         = NArgs.SetOf.value
        self._name_   : str  = cast( str, NArgs.SetOf.name )
        self._count_  : int  = count
        self._optional: bool = NArgs.SetOf.optional
        self._type    : Union[ Type[ int ], Type[ str ]] = NArgs.SetOf.type

    @property
    def type( self ) -> Union[ Type[ int ], Type[ str ]]:
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


ERR_MSG_UNSUPPORTED_TYPE: Final[ str ] = \
    "NArgs does not support type '%s'"

class NArgs( NumberOfArguments, Enum ):
    SetOf        = ( None, type( int ), False )
    OneOptional  = ( "?",  type( str ), True  )
    Many         = ( "+",  type( str ), False )
    ManyOptional = ( "*",  type( str ), True  )

    @staticmethod
    def parse( value ) -> Optional[ NumberOfArguments ]:
        if   ( value is None ):
               return None
        elif ( isinstance( value, int )):
               return CArgs( value )
        elif ( isinstance( value, str )):
               return NArgs( value ) # type: ignore
        else:  raise TypeError( ERR_MSG_UNSUPPORTED_TYPE % type( value ))

    def __new__( cls, value, type, optional ):
        obj         = object.__new__( cls )
        obj._value_ = value
        obj._count_ = None
        return obj

    def __init__( self, value, type, optional ):
        self._optional = optional
        self._type     = type

    def __call__( self, value ):
        return super().__call__( value )

    @property
    def type( self ) -> Union[ Type[ int ], Type[ str ]]:
        return self._type

    @property
    def optional( self ) -> bool:
        return self._optional
