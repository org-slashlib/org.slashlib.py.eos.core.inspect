# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect.py   is  distributed  WITHOUT ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' """
from unittest       import TestCase

class Test_Library_Exports( TestCase ):
    """ test if library exports are complete """

    def test_import_iscallable( self ):
        """
            test if function 'iscallable' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import iscallable

    def test_import_isclass( self ):
        """
            test if function 'isclass' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isclass

    def test_import_isclassmethod( self ):
        """
            test if function 'isclassmethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isclassmethod

    def test_import_isfunction( self ):
        """
            test if function 'isfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isfunction

    def test_import_ismethod( self ):
        """
            test if function 'ismethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethod

    def test_import_ismethodorfunction( self ):
        """
            test if function 'ismethodorfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethodorfunction

    def test_import_isstaticmethod( self ):
        """
            test if function 'isstaticmethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isstaticmethod
