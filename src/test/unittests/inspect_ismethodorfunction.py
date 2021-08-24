# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_ismethodorfunction.py  is distributed WITHOUT  ANY WARRANTY; without
#   even the  implied warranty  of MERCHANTABILITY  or FITNESS FOR  A PARTICULAR
#   PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'ismethodorfunction' """
from unittest   import TestCase

class Test_Module_inspect_ismethodorfunction( TestCase ):

    def test_import_ismethodorfunction( self ):
        """
            test if function 'ismethodorfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethodorfunction

    def test_ismethodorfunction( self ):
        """
            test function 'ismethodorfunction'
        """
        from org.slashlib.py.eos.core.inspect import ismethodorfunction

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
        self.assertTrue( ismethodorfunction( testfunction ))

        self.assertIsNotNone( TestClass.clsmethod )
        self.assertTrue( ismethodorfunction( TestClass.clsmethod ))

        self.assertIsNotNone( TestClass.statmethod )
        self.assertTrue( ismethodorfunction( TestClass.statmethod ))

        self.assertIsNotNone( TestClass.testmethod )
        self.assertTrue( ismethodorfunction( TestClass.testmethod   ))
        self.assertTrue( ismethodorfunction( TestClass().testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertFalse( ismethodorfunction( TestClass ))
