# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_utils.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
from   gettext                          import gettext
from   typing                           import Any
from   typing                           import Final
from   typing                           import Optional
from   typing                           import Tuple
from   typing                           import Type
from   typing                           import Union
from   typing                           import cast
from   typing                           import get_args
from   typing                           import get_type_hints

def get_property_name( prop: Optional[ property ]) -> Optional[ str ]:
    """ return property name from getter function """
    if  ( not ( prop is None )) and \
        ( not ( prop.fget is None )):
          return prop.fget.__name__
    else: return None

NAMEANDFLAGPATTERN: Final[ str ] = "-%s"

def get_flag_and_name( prop: Optional[ property ]) -> Optional[ Tuple[ str, ... ]]:
    """ convert property name to argument name or flag """
    propname = get_property_name( prop )
    if  ( not ( propname is None )):
          flag = "-%s" % propname[ 0 ]
          name = "-%s" % propname
          return ( flag, name )
    else: return None

def get_help_string( prop: Optional[ property ]) -> Optional[ str ]:
    """ retrieve __doc__ string from property and use it as help string """
    return None if ( prop is None ) else prop.__doc__

STR_RETURN: Final[ str ] = "return"

def get_return_type( prop: Optional[ property ]) -> Optional[ Union[ Type, Tuple[ Type, ... ]]]:
    """ retrieve return type property.fget annotation and use it as "type" """
    if  ( not ( prop is None )) and ( not ( prop.fget is None )):
          try :
                 returntypes = get_type_hints( prop.fget )[ STR_RETURN ]
                 asargs      = get_args( returntypes )
                 if  ( len( asargs ) == 0 ):
                       return returntypes # returntypes is [ str | int | ... ]
                 else: return asargs # returntypes is [ Optional | Union | ... ]
          except KeyError: return None # KeyError: 'return'
    else: return None
