# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument_utils.py  is distributed WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
import re
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

# TODO ... see argumentparser for prefix_chars?
FLAGPATTERN: Final[ str ] = "-%s"
NAMEPATTERN: Final[ str ] = "--%s"

def get_flag_and_name( prop: Optional[ property ]) -> Optional[ Tuple[ str, ... ]]:
    """ convert property name to argument name or flag """
    propname = get_property_name( prop )
    if  ( not ( propname is None )):
          flag = FLAGPATTERN % propname[ 0 ]
          name = NAMEPATTERN % propname
          return ( flag, name )
    else: return None

def get_dest_from_arg( argument: str ) -> str:
    return re.sub( r"-", "_", re.sub( r"^-*", "", argument ))

def get_help_string( prop: Optional[ property ]) -> Optional[ str ]:
    """ retrieve __doc__ string from property and use it as help string """
    return None if ( prop is None ) else prop.__doc__

STR_RETURN: Final[ str ] = "return"

def get_return_type( prop: Optional[ property ]) -> Optional[ Union[ Tuple[ Type, ... ]]]:
    """ retrieve return type property.fget annotation and use it as "type" """
    if  ( not ( prop is None )) and ( not ( prop.fget is None )):
          try :
                 returntypes = get_type_hints( prop.fget )[ STR_RETURN ]
                 asargs      = get_args( returntypes )
                 returntuple = None
                 if  ( len( asargs ) == 0 ):
                       returntuple = returntypes # returntypes is [ str | int | ... ]
                 else: returntuple = asargs # returntypes is [ Optional | Union | ... ]

                 if  ( not ( returntuple is None )):
                       returntuple = returntuple if isinstance( returntuple, tuple ) else ( returntuple, )
                 else: pass

                 return returntuple
          except KeyError: return None # KeyError: 'return'
    else: return None
