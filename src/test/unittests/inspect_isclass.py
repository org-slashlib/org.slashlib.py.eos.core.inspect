# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_isclass.py  is distributed WITHOUT ANY  WARRANTY; without even the
#   implied  warranty of MERCHANTABILITY  or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isclass' """
from unittest   import TestCase

class Test_Module_inspect_isclass( TestCase ):

    def test_import_isclass( self ):
        """
            test if function 'isclass' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isclass

    def test_isclass( self ):
        """
            test function 'isclass'
        """
        from org.slashlib.py.eos.core.inspect import isclass

        def testfunction():
            pass

        class TestClass():
            @classmethod
            def clsmethod( cls ):
                pass

            @staticmethod
            def statmethod():
                pass

            def testmethod( self ):
                pass

        self.assertIsNotNone( testfunction )
        self.assertFalse( isclass( testfunction ))

        self.assertIsNotNone( TestClass.clsmethod )
        self.assertFalse( isclass( TestClass.clsmethod ))

        self.assertIsNotNone( TestClass.statmethod )
        self.assertFalse( isclass( TestClass.statmethod ))

        self.assertIsNotNone( TestClass.testmethod )
        self.assertFalse( isclass( TestClass.testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertTrue(  isclass( TestClass    ))
