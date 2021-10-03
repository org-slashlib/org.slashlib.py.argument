# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   action.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.
#
from enum       import auto
from enum       import Enum
from typing     import Optional

class Action( Enum ):
    Append      = "append"
    AppendConst = "append_const"
    Count       = "count"
    Extend      = "extend"
    Help        = "help"
    Store       = "store"
    StoreConst  = "store_const"
    StoreFalse  = "store_false"
    StoreTrue   = "store_true"
    Version     = "version"

    @staticmethod
    def parse( value: str ) -> Optional[ 'Action' ]:
        """ Returns an Enumeration from 'value' or None """
        if  ( not ( value is None )):
              value = str( value ).lower()
              for enum in Action:
                  if  ( value == enum.name.lower()) or \
                      ( value == enum.value.lower()):
                        return enum
                  else: continue
              return None
        else: return None

    def __str__( self ):
        """
            Make sure, the string conversion of an enumeration
            returns its stringified value
        """
        return str( self.value )
