# -*- encoding: utf-8 -*-
#
#   © 2021, slashlib.org.
#
#   inspect_isclass.py  is distributed WITHOUT ANY  WARRANTY; without even the
#   implied  warranty of MERCHANTABILITY  or FITNESS FOR A PARTICULAR PURPOSE.
#
""" tests for package 'org.slashlib.py.eos.core.inspect' - 'isclass' """
from unittest   import TestCase

class Test_Module_inspect_iscallable( TestCase ):

    def test_import_iscallable( self ):
        """
            test if function 'iscallable' can be imported from
            'org.slashlib.py.eos.core.inspect'
        """
        from org.slashlib.py.eos.core.inspect import iscallable

    def test_iscallable_on_function( self ):
        """
            test function 'iscallable' on function
        """
        from org.slashlib.py.eos.core.inspect import iscallable

        def testfunction():
            pass

        self.assertIsNotNone( testfunction )
        self.assertTrue( iscallable( testfunction ))

    def test_iscallable_on_method( self ):
        """
            test function 'iscallable' on methods of classes (unbound & bound)
        """
        from org.slashlib.py.eos.core.inspect import iscallable

        class TestClass():

            def testmethod( self ):
                pass

        self.assertIsNotNone( TestClass.testmethod )
        self.assertTrue( iscallable( TestClass.testmethod ))

        test = TestClass()

        self.assertIsNotNone( test.testmethod )
        self.assertTrue( iscallable( test.testmethod ))

    def test_iscallable_on_class( self ):
        """
            test function 'iscallable' on simple class
        """
        from org.slashlib.py.eos.core.inspect import iscallable

        class TestClass():
              pass

        self.assertIsNotNone( TestClass )
        self.assertFalse( iscallable( TestClass ))

        test = TestClass()

        self.assertIsNotNone( test )
        self.assertFalse( iscallable( test ))

    def test_iscallable_on_callable_class( self ):
        """
            test function 'iscallable' on callable class
        """
        from org.slashlib.py.eos.core.inspect import iscallable

        class TestClass():

            def __call__( self ):
                pass

        self.assertIsNotNone( TestClass )
        self.assertTrue( iscallable( TestClass ))

        test = TestClass()

        self.assertIsNotNone( test )
        self.assertTrue( iscallable( test ))
