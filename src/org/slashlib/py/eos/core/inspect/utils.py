# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   utils.py  is distributed WITHOUT ANY WARRANTY; without even the implied
#   warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A PARTICULAR  PURPOSE.
#
""" provides utility functions for inspections """

EMPTY  = ""
LOCALS = ".<locals>."

def get_local_part( qname: str ) -> str:
    """
        Returns the 'local' part of qualified names

        Example:
            print( get_local_part( "foo" ))
            # => foo
            print( get_local_part( "Foo.bar" ))
            # => Foo.bar
            print( get_local_part( "foo.<locals>.Bar.baz" ))
            # => Bar.baz
    """
    qname = EMPTY if qname is None else qname
    return qname.rsplit( LOCALS, 1 )[ -1 ]
