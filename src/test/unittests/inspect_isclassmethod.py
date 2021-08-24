# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_isclassmethod.py  is distributed  WITHOUT ANY WARRANTY; without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isclassmethod' """
from unittest   import TestCase

class Test_Module_inspect_isclassmethod( TestCase ):

    def test_import_isclassmethod( self ):
        """
            test if function 'isclassmethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isclassmethod

    def test_isclassmethod( self ):
        """
            test function 'isclassmethod'
        """
        from org.slashlib.py.eos.core.inspect import isclassmethod

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
        self.assertFalse( isclassmethod( None,        testfunction ))
        self.assertFalse( isclassmethod( TestClass,   testfunction ))
        self.assertFalse( isclassmethod( TestClass(), testfunction ))

        self.assertIsNotNone( TestClass.clsmethod )
        self.assertTrue(  isclassmethod( TestClass,   TestClass.clsmethod ))
        self.assertTrue(  isclassmethod( TestClass(), TestClass.clsmethod ))

        self.assertIsNotNone( TestClass.statmethod )
        self.assertFalse( isclassmethod( TestClass,   TestClass.statmethod ))
        self.assertFalse( isclassmethod( TestClass(), TestClass.statmethod ))

        self.assertIsNotNone( TestClass.testmethod )
        self.assertFalse( isclassmethod( TestClass,   TestClass.testmethod   ))
        self.assertFalse( isclassmethod( TestClass(), TestClass().testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertFalse( isclassmethod( TestClass,   TestClass ))
        self.assertFalse( isclassmethod( TestClass(), TestClass ))
