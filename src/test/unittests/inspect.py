# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect.py   is  distributed  WITHOUT ANY  WARRANTY;  without  even  the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' """
from __future__     import absolute_import
from unittest       import TestCase

class Test_Module_Inspect( TestCase ):

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

    def test_import_isfunction( self ):
        """
            test if function 'isfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isfunction

    def test_isfunction( self ):
        """
            test function 'isfunction'
        """
        from org.slashlib.py.eos.core.inspect import isfunction

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

        # standalone 'def funct()' are 'functions'
        self.assertIsNotNone( testfunction )
        self.assertTrue( isfunction( testfunction ))

        # @classmethod 'def funct( cls )' are NOT 'functions'
        self.assertIsNotNone( TestClass.clsmethod )
        self.assertFalse( isfunction( TestClass.clsmethod ))

        # @staticmethod 'def funct()' are 'functions'
        self.assertIsNotNone( TestClass.statmethod )
        self.assertTrue( isfunction( TestClass.statmethod ))

        # class: 'def funct()' are 'functions' as long as they are not bound
        self.assertIsNotNone( TestClass.testmethod )
        self.assertTrue(  isfunction( TestClass.testmethod   ))
        self.assertFalse( isfunction( TestClass().testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertFalse( isfunction( TestClass ))

    def test_import_ismethod( self ):
        """
            test if function 'ismethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethod

    def test_ismethod( self ):
        """
            test function 'ismethod'
        """
        from org.slashlib.py.eos.core.inspect import ismethod

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

        # standalone 'def funct()' are NOT 'methods'
        self.assertIsNotNone( testfunction )
        self.assertFalse( ismethod( testfunction ))

        # @classmethod 'def funct( cls )' are 'methods'
        self.assertIsNotNone( TestClass.clsmethod )
        self.assertTrue( ismethod( TestClass.clsmethod   ))
        self.assertTrue( ismethod( TestClass().clsmethod ))

        # @staticmethod 'def funct()' are NOT 'methods'
        self.assertIsNotNone( TestClass.statmethod )
        self.assertFalse( ismethod( TestClass.statmethod   ))
        self.assertFalse( ismethod( TestClass().statmethod ))

        # class: 'def funct()' are 'methods' if they are bound
        self.assertIsNotNone( TestClass.testmethod )
        self.assertFalse( ismethod( TestClass.testmethod   ))
        self.assertTrue(  ismethod( TestClass().testmethod ))

        self.assertIsNotNone( TestClass )
        self.assertFalse( ismethod( TestClass ))

    def test_import_ismethodorfunction( self ):
        """
            test if function 'ismethodorfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethodorfunction

    def test_ismethod( self ):
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
