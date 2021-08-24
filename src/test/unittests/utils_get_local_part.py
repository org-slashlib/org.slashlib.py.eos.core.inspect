# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   utils_get_local_part.py  is distributed  WITHOUT ANY WARRANTY;  without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isstaticmethod' """
from inspect    import isfunction
from unittest   import TestCase
from setuptools import setup
from setuptools import find_packages
import os

filemode    = "rb"
filecmd     = "exec"
localfile   = os.path.join( "src", "org", "slashlib", "py", "eos", "core", "inspect", 'utils.py' )
exec( compile( open( localfile, filemode ).read(), localfile, filecmd ))

class Test_Module_utils_get_local_part( TestCase ):

    def test_import_get_local_part( self ):
        """
            test if function 'get_local_part' can be imported from
            module 'org.slashlib.py.eos.core.inspect.utils'
        """
        self.assertIsNotNone( get_local_part )
        self.assertTrue( isfunction( get_local_part ))

    def test_get_local_part_on_missing_argument( self ):
        """
            test if function 'get_local_part' raises a TypeError on missing
            postional argument.
        """
        with self.assertRaises( TypeError ):
             get_local_part( )

    def test_get_local_part_on_None( self ):
        """ test behaviour of function 'get_local_part' on None """
        self.assertTrue( get_local_part( None ) == "" )

    def test_get_local_part_on_Empty( self ):
        """ test behaviour of function 'get_local_part' on '' (empty string) """
        self.assertTrue( get_local_part( "" ) == "" )

    def test_get_local_part_on_foo( self ):
        """ test behaviour of function 'get_local_part' on 'foo' """
        self.assertTrue( get_local_part( "foo" ) == "foo" )

    def test_get_local_part_on_foo_bar( self ):
        """ test behaviour of function 'get_local_part' on 'foo.bar' """
        self.assertTrue( get_local_part( "foo.bar" ) == "foo.bar" )

    def test_get_local_part_on_foo_locals_bar( self ):
        """ test behaviour of function 'get_local_part' on 'foo.<locals>.bar' """
        self.assertTrue( get_local_part( "foo.<locals>.bar" ) == "bar" )

    def test_get_local_part_on_foo_locals_bar_baz( self ):
        """ test behaviour of function 'get_local_part' on 'foo.<locals>.bar.baz' """
        self.assertTrue( get_local_part( "foo.<locals>.bar.baz" ) == "bar.baz" )
