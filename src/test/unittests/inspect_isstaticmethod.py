# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_isstaticmethod.py  is distributed WITHOUT ANY WARRANTY; without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isstaticmethod' """
from unittest   import TestCase

class Test_Module_inspect_isstaticmethod( TestCase ):

    def test_import_isstaticmethod( self ):
        """
            test if function 'isstaticmethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isstaticmethod

    def test_isstaticmethod( self ):
        """
            test function 'isstaticmethod'
        """
        from org.slashlib.py.eos.core.inspect import isstaticmethod

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
        self.assertFalse( isstaticmethod( None,        testfunction ))
        self.assertFalse( isstaticmethod( TestClass,   testfunction ))
        self.assertFalse( isstaticmethod( TestClass(), testfunction ))

        self.assertIsNotNone( TestClass.clsmethod )
        self.assertFalse( isstaticmethod( TestClass,   TestClass.clsmethod ))
        self.assertFalse( isstaticmethod( TestClass(), TestClass.clsmethod ))

        self.assertIsNotNone( TestClass.statmethod )
        self.assertTrue(  isstaticmethod( TestClass,   TestClass.statmethod ))
        self.assertTrue(  isstaticmethod( TestClass(), TestClass.statmethod ))

        self.assertIsNotNone( TestClass.testmethod )
        self.assertFalse( isstaticmethod( TestClass,   TestClass.testmethod   ))
        self.assertFalse( isstaticmethod( TestClass(), TestClass().testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertFalse( isstaticmethod( TestClass,   TestClass ))
        self.assertFalse( isstaticmethod( TestClass(), TestClass ))
