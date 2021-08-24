# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" provides extended inspection functions """
from   __future__   import absolute_import

import inspect
from   typing       import Any
from   typing       import Callable
from   typing       import cast
from   typing       import Type
from   typing       import TypeVar

from   .utils       import get_local_part

CALL = "__call__"
DOT  = "."

def iscallable( arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is callable (provides '__call__'); False otherwise
    """
    # note: return hasattr( arg, CALL ) returns true for all classes, which is
    #       not what we want.
    return CALL in dir( arg )

T = TypeVar( 'T' )

def isclass( arg: Type[ T ]) -> bool:
    """
        Returns:
            True, if arg is of type {class}; False otherwise
    """
    return inspect.isclass( arg )

def ismethodorfunction( arg: Callable  ) -> bool:
    """
        Returns:
            True, if arg is of type {method} or {function}; False otherwise
    """
    return inspect.ismethod( arg ) or inspect.isfunction( arg )

def _ismethod( arg: Callable ) -> bool:
    """
        Internal helper function.

        Returns:
            True, if arg is of type {method}; False otherwise
    """
    return get_local_part( arg.__qualname__ ).endswith( DOT + arg.__name__ )

def ismethod( arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is of type {method}; False otherwise
    """
    return ismethodorfunction( arg ) and _ismethod( arg )

def _isfunction( arg: Callable ) -> bool:
    """
        Internal helper function.

        Returns:
            True, if arg is of type {function}; False otherwise
    """
    return inspect.isfunction( arg ) and ( get_local_part( arg.__qualname__ ) == arg.__name__ )

def isfunction( arg: Callable ) -> bool:
    """
        Functions, which are not and will not become bound members of classes,
        are defined to be pyeos functions.

        Returns:
            True, if arg is of type {function}; False otherwise
    """
    return ( not inspect.ismethod( arg )) and _isfunction( arg )

def isstaticmethod( cls: Type[ T ], arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is of type '@staticmethod def funct()'; False otherwise
    """
    if  ( ismethodorfunction( arg )):
          try:
              # make sure, this works even without type checking
              cls      = cls if isclass( cls ) else cast( Any, cls ).__class__
              argname  = arg.__name__
              statattr = inspect.getattr_static( cls, argname )
              return isinstance( statattr, staticmethod ) and \
                     ( cls.__qualname__ + "." + argname  == arg.__qualname__ )
          except AttributeError as e:
              return False
    else: return False

def isclassmethod( cls: Type[ T ], arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is of type '@classmethod def funct()'; False otherwise
    """
    if  ( inspect.ismethod( arg )):
          # make sure, this works even without type checking
          cls = cls if isclass( cls ) else cast( Any, cls ).__class__
          return cast( Any, arg ).__self__ is cls
    else: return False
