# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_ismethod.py  is  distributed WITHOUT ANY WARRANTY; without even the
#   implied  warranty of  MERCHANTABILITY or FITNESS  FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'ismethod' """
from unittest   import TestCase

def testfunction():
    pass

class Test_Module_inspect_ismethod( TestCase ):

    def test_import_ismethod( self ):
        """
            test if function 'ismethod' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import ismethod

    def test_ismethod_on_function( self ):
        """
            test function 'ismethod' on function
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        # standalone 'def funct()' are NOT (python) 'methods' because unbound
        # standalone 'def funct()' are not members of classes and no pyeos methods
        self.assertIsNotNone( testfunction )
        self.assertFalse( ismethod( testfunction ))

    def test_ismethod_on_local_function( self ):
        """
            test function 'ismethod' on local function
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        def testfunction():
            pass

        # standalone 'def funct()' are NOT (python) 'methods' because unbound
        # standalone 'def funct()' are not members of classes and no pyeos methods
        self.assertIsNotNone( testfunction )
        self.assertFalse( ismethod( testfunction ))

    def test_ismethod_on_inner_function( self ):
        """
            test function 'ismethod' on inner function
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        def testfunction():
            def innerfunction():
                pass
            return innerfunction

        # standalone 'def funct()' are NOT (python) 'methods' because unbound
        # standalone 'def funct()' are not members of classes and no pyeos methods
        self.assertIsNotNone( testfunction )
        self.assertFalse( ismethod( testfunction()))

    def test_ismethod_on_class( self ):
        """
            test function 'ismethod' on class
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        class TestClass():
            pass

        self.assertIsNotNone( TestClass )
        self.assertFalse( ismethod( TestClass ))

    def test_ismethod_on_classmethod( self ):
        """
            test function 'ismethod' on classmethod
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        class TestClass():
            @classmethod
            def clsmethod( cls ):
                pass

        # @classmethod 'def funct( cls )' are (python) 'methods' because
        #              they are bound (to a class).
        # @classmethod(s) are class members and therefore pyeos methods
        self.assertIsNotNone( TestClass.clsmethod )
        self.assertTrue( ismethod( TestClass.clsmethod   ))
        self.assertTrue( ismethod( TestClass().clsmethod ))

    def test_ismethod_on_staticmethod( self ):
        """
            test function 'ismethod' on staticmethod
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        class TestClass():

            @staticmethod
            def statmethod():
                pass

        # @staticmethod 'def funct()' are NOT (python) 'methods' because
        #               they are bound.
        # @staticmethod(s) are class members and therefore no pyeos methods
        self.assertIsNotNone( TestClass.statmethod )
        self.assertTrue( ismethod( TestClass.statmethod   ))
        self.assertTrue( ismethod( TestClass().statmethod ))


    def test_ismethod_on_method( self ):
        """
            test function 'ismethod' on method
        """
        from org.slashlib.py.eos.core.inspect import ismethod

        class TestClass():

            def testmethod( self ):
                pass

        # @staticmethod 'def funct()' are NOT (python) 'methods' as long as
        #               they are not bound.
        # functions which are class members are pyeos methods
        self.assertIsNotNone( TestClass.testmethod )
        self.assertTrue( ismethod( TestClass.testmethod   ))
        self.assertTrue( ismethod( TestClass().testmethod ))
