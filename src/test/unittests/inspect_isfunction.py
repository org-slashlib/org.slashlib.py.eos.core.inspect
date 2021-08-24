# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_isfunction.py  is  distributed  WITHOUT  ANY  WARRANTY; without even
#   the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isfunction' """
from unittest   import TestCase

def testfunction():
    pass

class Test_Module_inspect_isfunction( TestCase ):

    def test_import_isfunction( self ):
        """
            test if function 'isfunction' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import isfunction

    def test_isfunction_on_function( self ):
        """
            test function 'isfunction' on function
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        # standalone 'def funct()' are 'functions'
        self.assertIsNotNone( testfunction )
        self.assertTrue( isfunction( testfunction ))

    def test_isfunction_on_local_function( self ):
        """
            test function 'isfunction' on local function
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        def testfunction():
            pass

        # standalone 'def funct()' are 'functions'
        self.assertIsNotNone( testfunction )
        self.assertTrue( isfunction( testfunction ))

    def test_isfunction_on_inner_function( self ):
        """
            test function 'isfunction' on inner function
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        def testfunction():
            def innerfunction():
                pass
            return innerfunction

        # standalone 'def funct()' are (python) 'functions' andy pyeos functions
        self.assertIsNotNone( testfunction )
        self.assertTrue( isfunction( testfunction()))

    def test_isfunction_on_class( self ):
        """
            test function 'isfunction'
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        class TestClass():
            pass

        self.assertIsNotNone( TestClass )
        self.assertFalse( isfunction( TestClass ))

    def test_isfunction_on_classmethod( self ):
        """
            test function 'isfunction' on classmethod
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        class TestClass():
            @classmethod
            def clsmethod( cls ):
                pass

        # @classmethod 'def funct( cls )' are NOT (python) 'functions' because
        #              they are bound (to a class).
        # @classmethod(s) are class members and therefore no pyeos functions
        self.assertIsNotNone( TestClass.clsmethod )
        self.assertFalse( isfunction( TestClass.clsmethod ))


    def test_isfunction_on_staticmethod( self ):
        """
            test function 'isfunction' on staticmethod
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        class TestClass():

            @staticmethod
            def statmethod():
                pass

        # @staticmethod 'def funct()' are (python) 'functions'
        # @staticmethod(s) are class members and therefore no pyeos functions
        self.assertIsNotNone( TestClass.statmethod )
        self.assertFalse( isfunction( TestClass.statmethod ))

    def test_isfunction_on_method( self ):
        """
            test function 'isfunction' on method
        """
        from org.slashlib.py.eos.core.inspect import isfunction

        class TestClass():

            def testmethod( self ):
                pass

        # class: 'def funct()' are (python) 'functions' as long as not bound
        # functions which are class members are not pyeos functions
        self.assertIsNotNone( TestClass.testmethod )
        self.assertFalse( isfunction( TestClass.testmethod   ))
        self.assertFalse( isfunction( TestClass().testmethod ))
