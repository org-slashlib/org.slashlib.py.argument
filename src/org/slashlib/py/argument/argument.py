# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   argument.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# import logging
# LOGGER: Final[ Any ] = logging.getLogger( __name__ )
from gettext                            import gettext
from typing                             import cast
from typing                             import Final
from typing                             import Optional
from typing                             import Tuple
from typing                             import Type
from typing                             import Union

from org.slashlib.py.argument.parser    import register
from org.slashlib.py.argument.types     import Action
from org.slashlib.py.argument.types     import NArgs
from org.slashlib.py.argument.types     import NumberOfArguments
from org.slashlib.py.argument.typing    import ArgumentDecorator
from org.slashlib.py.argument.typing    import ArgumentParser

from .argument_utils                    import get_flag_and_name
from .argument_utils                    import get_help_string
from .argument_utils                    import get_property_name
from .argument_utils                    import get_return_type

ERR_MSG_PARAMETER_PROPERTY_TYPE: Final[ str ] = \
    "Argument.__call__: Parameter 'prop' must be of type 'property'"
ERR_MSG_NO_FLAG_OR_NAME: Final[ str ] = \
    "@Argument cannot determine 'flag' or 'name' for property '%s'."
ERR_MSG_NO_HELP_TEXT: Final[ str ] = \
    "@Argument cannot determine help text from __doc__ string of property '%s'."
ERR_MSG_AMBIGUOUS_HELP_TEXT: Final[ str ] = \
    "Different help texts found in @Argument parameter 'help' and __doc__ string of property '%s'."
ERR_MSG_NO_RETURN_TYPE: Final[ str ] = \
    "@Argument cannot determine return type for property '%s'. Return type missing."
ERR_MSG_MULTIPLE_RETURN_TYPES: Final[ str ] = \
    "@Argument cannot determine return type for property '%s'. Too many possible types."
ERR_MSG_RETURN_TYPE_MISMATCH: Final[ str ] = \
    "Returntype missmatch: @Arguments( type='%s' ) does not match property '%s's return type(s) '%s'."
ERR_MSG_OPTIONAL_MISMATCH: Final[ str ] = \
    "Missmatch between @Arguments( nargs='%s' ) and property '%s's return type (optional vs. mandatory)."
ERR_MSG_ELEMENT_AFTER_PROPERTY: Final[ str ] = \
    "Argument.__init__: Supernumerary positional argument after argument of type 'property'"
ERR_MSG_ELEMENT_AFTER_STR: Final[ str ] = \
    "Argument.__init__: Supernumerary positional argument after argument of type 'str'"
ERR_MSG_TYPE_OF_POSITIONAL_ARGUMENTS: Final[ str ] = \
    "Argument.__init__: Positional argument(s) must be of type 'property' or 'str'"
ERR_MSG_DELETER_NOT_SUPPORTED: Final[ str ] = \
    "Argument.deleter is not supported. Arguments are expected to return a (default) value or {None}."
ERR_MSG_DECORATOR_ACCESS_PERMITTED: Final[ str ] = \
    "decorator access permitted"
ERR_MSG_PROPERTY_ACCESS_PERMITTED: Final[ str ] = \
    "property access permitted"
ERR_MSG_UNREADABLE_ATTRIBUTE: Final[ str ] = \
    "unreadable attribute"

class Argument( property, ArgumentDecorator ):
    """
        @Argument can be used for decorating properties, that should be recognized as command-line arguments.
        @Argument is a decorator with optional arguments, which help in compleating or overwriting values,
        that can be collected from the decorated property.
        @Argument internally makes use of pythons argparse module and a replacement of:
        <code>argparse.add_argument( ... )</code>.

        Example:
            class MyClass():
                @Argument
                @property
                def whatever
                    '''used for whatever'''

            # python myexample.py -h
            # usage: myexample.py [-h] [-w, --whatever]
            # optional arguments:
            # -h, --help        show this help message and exit
            # -w. --whatever    used for whatever

    """
    def __init__( self, *args: Union[ property, str ],
                  group:    Optional[ str  ] = None,
                  action:   Optional[ str  ] = None,
                  nargs:    Optional[ Union[ int, str ]] = None,
                  const:    Optional[ Union[ bool, int, float, str ]] = None,
                  default:  Optional[ Union[ bool, int, float, str ]] = None,
                  type:     Optional[ Union[ Type[ bool ], Type[ int ], Type[ float ], Type[ str ]]] = None,
                  choices:  Optional[ Tuple[ Union[ bool, int, float, str ], ... ]] = None,
                  required: Optional[ bool ] = None, help: Optional[ str ] = None,
                  metavar:  Optional[ str  ] = None, dest: Optional[ str ] = None ) -> None:
        """
            Args:
                args:           Either a name or a list of option strings, e.g.
                                foo or -f, --foo. In case this value is not
                                provided, @Argument will us the property name.
                group:          Name of a mutual exclusive group of arguments.
                action:         The basic type of action to be taken when this
                                argument is encountered at the command line.
                nargs:          The number of command-line arguments that should
                                be consumed.
                const:          A constant value required by some action and
                                nargs selections.
                default:        The value produced if the argument is absent
                                from the command line and if it is absent from
                                the namespace object.
                type:           The type to which the command-line argument
                                should be converted.
                choices:        A container of the allowable values for the
                                argument.
                required:       Whether or not the command-line option may be
                                omitted (optionals only).
                help:           A brief description of what the argument does.
                metavar:        A name for the argument in usage messages.
                dest:           The name of the attribute to be added to the
                                object returned by <code>parse_args()</code>
        """
        self._prop: Optional[ property ] = None
        self._propertyname: Optional[ str ] = None
        self._nameorflags: Optional[ Tuple[ str, ... ]] = None

        self.__init___prop( *args )
        self.__init___nameorflags( *args )

        # at this point one of [ self_prop, self._nameorflags] must not be None!
        if (( self._prop is self._nameorflags is None ) and
            ( len ( args ) > 0 )):
              raise TypeError( gettext( ERR_MSG_TYPE_OF_POSITIONAL_ARGUMENTS ))
        else: pass

        try:
                self.__init__keywordargs( group   = group,
                     action  = Action.parse( action ),
                     nargs   = NArgs.parse( nargs ), const = const,
                     default = default, type     = type,
                     choices = choices, required = required,
                     metavar = metavar, dest     = dest )
        except ValueError as err:
                raise TypeError( "@Argument: invalid parameter." ) from err

        self._consolidate_by_property( self._prop )

    def __init___prop( self, *args: Union[ property, str ]):
        """
            Initialize member self._prop from positional arguments.
        """
        count: int = len( args )
        if  ( count > 0 ) and ( isinstance( args[ 0 ], property )):
              if  ( count == 1 ):
                    prop: property     = args[ 0 ]
                    self._prop         = prop
                    self._propertyname = get_property_name( prop )
                    self._nameorflags  = None
              else: raise AttributeError( gettext( ERR_MSG_ELEMENT_AFTER_PROPERTY ))
        else: pass

    def __init___nameorflags( self, *args: Union[ property, str ]):
        """
            Initialize member self._nameorflags from positional arguments.
        """
        if  ( len( args ) > 0 ) and ( isinstance( args[ 0 ], str )):
              for value in args:
                  if  ( not isinstance( value, str )):
                        raise TypeError( gettext( ERR_MSG_ELEMENT_AFTER_STR ))
                  else: continue
              self._prop         = None
              self._propertyname = None
              self._nameorflags  = cast( Tuple[ str, ... ], args )
        else: pass

    def __init__keywordargs( self,
        group:    Optional[ str  ] = None,
        action:   Action = Action.Store,
        nargs:    NumberOfArguments = None,
        const:    Optional[ Union[ bool, int, float, str ]] = None,
        default:  Optional[ Union[ bool, int, float, str ]] = None,
        type:     Optional[ Union[ Type[ bool ], Type[ int ], Type[ float ], Type[ str ]]] = None,
        choices:  Optional[ Tuple[ Union[ bool, int, float, str ], ... ]] = None,
        required: Optional[ bool ] = None, help: Optional[ str ] = None,
        metavar:  Optional[ str  ] = None, dest: Optional[ str ] = None ):
        """
            Initialize members from keyword arguments.
        """
        self._group:    Optional[ str  ]    = group
        self._action:   Action              = action
        self._nargs:    NumberOfArguments   = nargs
        self._const:    Optional[ Union[ bool, int, float, str ]]   = const
        self._default:  Optional[ Union[ bool, int, float, str ]]   = default
        self._type:     Optional[ Union[ Type[ bool ], Type[ int ], Type[ float ], Type[ str ]]] = type
        self._choices:  Optional[ Tuple[ Union[ bool, int, float, str ], ... ]] = choices
        self._required: Optional[ bool ]    = required
        self._help:     Optional[ str  ]    = help
        self._metavar:  Optional[ str  ]    = metavar
        self._dest:     Optional[ str  ]    = dest

    def __get__( self, obj, objtype = None ):
        """
            Called if decorated property (getter) is accessed.
        """
        if    obj is None:
              raise AttributeError( gettext( ERR_MSG_DECORATOR_ACCESS_PERMITTED ))
        elif  self._prop is None:
              raise AttributeError( gettext( ERR_MSG_PROPERTY_ACCESS_PERMITTED ))
        elif  self._prop.fget is None:
              raise AttributeError( gettext( ERR_MSG_UNREADABLE_ATTRIBUTE ))
        else: return self._prop.fget( obj )

    def __call__( self, prop: property ) -> property:
        """
            Called if @Argument is called with arguments, like:
            @Argument( "some", "arguments" )

            Will result in the folowing call oder:
                @Argument.__init__
                @Argument.__call__
                @Argument.__get__
        """
        if  ( isinstance( prop, property )):
              self._prop = prop
              self._propertyname = get_property_name( prop )
              self._consolidate_by_property( prop )
              return self
        else: raise TypeError( gettext( ERR_MSG_PARAMETER_PROPERTY_TYPE ))

    def _consolidate_by_property( self, prop: Optional[ property ]):
        """
            Consolidate argument properties: 'flag', 'name', 'help', 'type' and 'required'.
        """
        #   Due to the nature of decorators, it is possible to either set values to decorator
        #   arguments or not. If set, such values must override data that can be derived from
        #   a property object. To make things more sophisticated, a property object itself
        #   may or may not provide the expected data.
        #   So, for example, a docstring has to be consolidated, after all possible ways of
        #   passing a docsting into this decorator can be considered (meaning: at a point in
        #   time, when there is no way left to call the decorator, such that property values
        #   or arguments might be subject to change by an additional input.)
        #   For a property decorator, this point in time has come, if the decorated property
        #   is passed to the decorator (which might happen in __init__ or in __call__).
        #
        #   Because @Argument implements the python descriptor interface, you can be sure one
        #   of both functions, either __init__ or __call__ will receive the decorated property
        #   (and this _will_ happen before __get__ is called!).
        #
        #   So this is the best point in time, to register the argument with an argument parser.

        if  ( not ( prop is None )):
              self._consolidate_flag_and_name( prop )
              self._consolidate_help( prop )
              self._consolidate_type_and_nargs( prop )
              # first step: register self {@Argument} as being available
              #             for use by an argument parser.
              register( self )
        else: pass

    def _consolidate_flag_and_name( self, prop: property ):
        """ set self._nameorflags, if not already set """
        if  ( self._nameorflags is None ) or ( len( self._nameorflags ) <= 0 ):
              flagandname = get_flag_and_name( prop )
              if  ( flagandname is None ):
                    raise AttributeError( gettext( ERR_MSG_NO_FLAG_OR_NAME ) % ( self._propertyname ))
              else: self._nameorflags = flagandname
        else: pass

    def _consolidate_help( self, prop: property ):
        """ set self._help, if not already set """
        help = get_help_string( prop )
        if  ( self._help is None ) and ( not ( help is None )):
              self._help = help
        elif( not ( self._help is None )) and ( not ( help is None )):
              if  ( not ( self._help == help )):
                    raise AttributeError( gettext( ERR_MSG_AMBIGUOUS_HELP_TEXT ) % ( self._propertyname ))
              else: pass
        elif( self._help is None ) and ( help is None ):
              raise AttributeError( gettext( ERR_MSG_NO_HELP_TEXT ) % ( self._propertyname ))
        else: pass

    def _consolidate_type_and_nargs( self, prop: property ):
        """ set self._type and self._required, if not already set """
        returntype = get_return_type( prop )
        isoptional = False

        if  ( not ( returntype is None )):
              returntype = returntype if isinstance( returntype, tuple ) else ( returntype, )
              nonetype   = type( None )
              isoptional = True if ( nonetype in returntype ) else False

              if  ( isoptional ):
                    returntype = [ tpe for tpe in returntype if not tpe is nonetype ]
              else: pass

              if  ( not ( self._type is None )):
                    # ( not ( returntype is None )) and ( not ( self._type is None ))
                    # check if self._type matches returntype from property.fget -> type:
                    if  ( not ( self._type in returntype )):
                          errormsg = gettext( ERR_MSG_RETURN_TYPE_MISMATCH ) % ( self._type, self._propertyname, str( returntype ))
                          raise TypeError( errormsg )
                    else: # self._type can be found in returntype therefor self._type is valid.
                          pass
              else: # ( not ( returntype is None )) and ( self._type is None )
                    # check if a useful return type can be found within tuple returntype
                    if  ( None in returntype ):
                          # None is already considered by 'isoptional' => remove None from returntypes
                          returntype  = tuple([ item for item in returntype if item is not None ])
                    else: pass

                    itemcount = len( returntype )
                    if  ( itemcount < 1 ):
                          raise AttributeError( gettext( ERR_MSG_NO_RETURN_TYPE ) % ( self._propertyname ))
                    elif( itemcount > 1 ):
                          raise AttributeError( gettext( ERR_MSG_MULTIPLE_RETURN_TYPES ) % ( self._propertyname ))
                    else: self._type = returntype[ 0 ]

        elif( self._type is None ):
              # ( self._type is None ) and ( returntype is None )
              raise AttributeError( gettext( ERR_MSG_NO_RETURN_TYPE ) % ( self._propertyname ))

        else: # ( not ( self._type is None )) and ( returntype is None )
              # this means self._type defines the return type
              pass

        if  ( not ( self._nargs is None )) and ( self._nargs.optional != isoptional ):
              raise AttributeError( gettext( ERR_MSG_OPTIONAL_MISMATCH ) % ( self._nargs, self._propertyname ))
        else: pass

    def _appendToParser( self, parser: ArgumentParser ):
        """ Append this @Argument to parsers arguments. """
        nmrflgs: Tuple[ str, ... ] = cast( Tuple, self._nameorflags )
        parser.addArgument( *nmrflgs,                      action   = self.action,   nargs = self.nargs,
                                   const   = self.const,   default  = self.default,  type  = self.type,
                                   choices = self.choices, required = self.required, help  = self.help,
                                   metavar = self.metavar, dest     = self.dest )

    def _appendToGroup( self, parser: ArgumentParser ):
        """ Append this @Argument to a mutual exclusive parser group. """
        nmrflgs: Tuple[ str, ... ] = cast( Tuple, self._nameorflags )
        group:   str               = cast( str, self.group )
        parser.addGroupedArgument( group,  *nmrflgs,       action   = self.action,   nargs = self.nargs,
                                   const   = self.const,   default  = self.default,  type  = self.type,
                                   choices = self.choices, required = self.required, help  = self.help,
                                   metavar = self.metavar, dest     = self.dest )

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
        # second step: get called and append...
        # note: this is not triggered asynchronous!
        if  ( self.grouped ):
              self._appendToGroup(  parser )
        else: self._appendToParser( parser )

    @property
    def action( self ) -> str:
        """ Returns @Argument 'action' in string format. """
        return Action.Store.value if self._action is None else self._action.value

    @property
    def choices( self ) -> Optional[ Tuple[ Union[ bool, int, float, str ], ... ]]:
        """ Returns @Argument 'choices'. """
        return self._choices

    @property
    def const( self ) -> Optional[ Union[ bool, int, float, str ]]:
        """ Returns @Argument 'const'. """
        return self._const

    @property
    def default( self ) -> Optional[ Union[ bool, int, float, str ]]:
        """ Returns @Argument 'default'. """
        return self._default

    @property
    def dest( self ) -> Optional[ str ]:
        """ Returns @Argument 'dest'. """
        return self._dest

    @property
    def group( self ) -> Optional[ str ]:
        """ Returns the actions group name, if set. """
        return self._group

    @property
    def grouped( self ) -> bool:
        """ Returns True, if a group name is set on @Argument. """
        return ( not ( self._group is None ))

    @property
    def help( self ) -> Optional[ str ]:
        """ Returns @Argument 'help'. """
        return self._help

    @property
    def metavar( self ) -> Optional[ str ]:
        """ Returns @Argument 'metavar'. """
        return self._metavar

    @property
    def nargs( self ) -> Optional[ Union[ int, str ]]:
        """ Returns @Argument 'nargs'. """
        return self._nargs if self._nargs is None else self._nargs.value

    @property
    def required( self ) -> Optional[ bool ]:
        """ Returns @Argument 'required'. """
        return self._required

    @property
    def type( self ) -> Optional[ Union[ Type[ bool ], Type[ int ], Type[ float ], Type[ str ]]]:
        """ Returns @Argument 'type'. """
        return self._type

    def setter( self, fset ):
        """
            Override superclass 'setter' to avoid creation of further @Argument.

            Note: superclass [property] uses
                  return type(self)(self.fget, fset, self.fdel, self.__doc__)
                  which would call constructor of class Argument
        """
        return type( self._prop )( self._prop.fget, fset, self._prop.fdel, self._prop.__doc__ )

    def deleter( self, fdel ):
        """
            Override superclass 'deleter' to avoid creation of deleter for @Argument.
            You wouldn't want someting like the following to happen on an argument:

            delete foo.bar
            argvalue = foo.bar
            >>> AttributeError: 'Foo' object has no attribute '_bar'

            If you want to delete an argument, set it to None and avoid defining a default value.
        """
        raise TypeError( gettext( ERR_MSG_DELETER_NOT_SUPPORTED ))
