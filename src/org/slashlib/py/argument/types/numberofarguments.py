# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   nargs.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty of  MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.
#
from abc                import abstractmethod
from typing             import Final
from typing             import Type
from typing             import Union

ERR_MSG_ABSTRACT_PROPERTY_TYPE    : Final[ str ] = "Called 'get' on abstract property 'type'"
ERR_MSG_ABSTRACT_PROPERTY_OPTIONAL: Final[ str ] = "Called 'get' on abstract property 'optional'"

class NumberOfArguments:
    @property
    @abstractmethod
    def type( self ) -> Union[ Type[ int ], Type[ str ]]:
        raise TypeError( ERR_MSG_ABSTRACT_PROPERTY_TYPE )

    @property
    @abstractmethod
    def optional( self ) -> bool:
        raise TypeError( ERR_MSG_ABSTRACT_PROPERTY_OPTIONAL )
