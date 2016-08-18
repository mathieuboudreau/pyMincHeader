import unittest
from pymincheader.pymincheader import PyMincHeader

class PyMincHeaderTest(unittest.TestCase):

    def setUp(self):
        self.badFileName = '_(238F.ds&.'
        self.goodFileName = 'demo/demo.mnc'
    def tearDown(self):
        pass

    def test_that_bad_filename_throws_exception(self):
        self.assertRaises(Exception,PyMincHeader,self.badFileName)

    def test_that_good_filename_stores_is_stored_on_init(self):
        demoHeader = PyMincHeader(self.goodFileName)
        self.assertEqual(demoHeader.fileName, 'demo/demo.mnc')
