# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect.py  is  distributed  WITHOUT  ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" defines utilities for use with decorators """
from   __future__   import absolute_import

import inspect
from   typing       import Any
from   typing       import Callable
from   typing       import cast
from   typing       import Type
from   typing       import TypeVar

T = TypeVar( 'T' )

def isclass( arg: Type[ T ]) -> bool:
    """
        Returns:
            True, if arg is of type {class}; False otherwise
    """
    return inspect.isclass( arg )

def ismethod( arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is of type {method}; False otherwise
    """
    return inspect.ismethod( arg )

def isfunction( arg: Callable ) -> bool:
    """
        Returns:
            True, if arg is of type {function}; False otherwise
    """
    return inspect.isfunction( arg )

def ismethodorfunction( arg: Callable  ) -> bool:
    """
        Returns:
            True, if arg is of type {method} or {function}; False otherwise
    """
    return ismethod( arg ) or isfunction( arg )

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
    if  ( ismethod( arg )):
          # make sure, this works even without type checking
          cls = cls if isclass( cls ) else cast( Any, cls ).__class__
          return cast( Any, arg ).__self__ is cls
    else: return False
