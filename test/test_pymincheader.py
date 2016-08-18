import unittest
from pymincheader.pymincheader import PyMincHeader

class PyMincHeaderTest(unittest.TestCase):

    def setUp(self):
        self.badFileName = '_(238F.ds&.'
        self.goodFileName = 'demo/demo.mnc'

        self.floatAttributeExample    = 'repetition'
        self.searchOutputFloatExample = {'attribute': 'acquisition:repetition_time', 'value': 2.3, 'line': 'acquisition:repetition_time = 2.3 ;'}

        self.stringAttributeExample   = 'series_description'
        self.searchOutputStringExample = {'attribute': 'acquisition:series_description', 'value': 'MPRAGE ADNI_iPAT2 ', 'line': 'acquisition:series_description = "MPRAGE ADNI_iPAT2 " ;'}

        self.nonExistingAttribute    = 'thisIS_Afake_At1ribute__/'
        self.searchOutputNonExistingExample = {'attribute': None, 'value': None, 'line': None}

    def tearDown(self):
        pass

    def test_that_bad_filename_throws_exception(self):
        self.assertRaises(Exception,PyMincHeader,self.badFileName)

    def test_that_good_filename_stores_is_stored_on_init(self):
        demoHeader = PyMincHeader(self.goodFileName)
        self.assertEqual(demoHeader.fileName, 'demo/demo.mnc')

    def test_that_verifies_output_keys_of_search_method_match_expected_keys_when_a_match_occurs(self):
        demoHeader = PyMincHeader('demo/demo.mnc')
        result = demoHeader.search(self.floatAttributeExample)
        self.assertEqual(result.keys(), self.searchOutputFloatExample.keys())

    def test_that_verifies_output_keys_of_search_method_match_expected_keys_when_there_is_no_match(self):
        demoHeader = PyMincHeader('demo/demo.mnc')
        result = demoHeader.search(self.nonExistingAttribute)
        self.assertEqual(result.keys(), self.searchOutputFloatExample.keys())

    def test_that_verifies_output_values_of_float_attribute_search_match_known_case(self):
        demoHeader = PyMincHeader('demo/demo.mnc')
        result = demoHeader.search(self.floatAttributeExample)

        for key in result.keys():
            self.assertEqual(result[key], self.searchOutputFloatExample[key])

    def test_that_verifies_output_values_of_string_attribute_search_match_known_case(self):
        demoHeader = PyMincHeader('demo/demo.mnc')
        result = demoHeader.search(self.stringAttributeExample)

        for key in result.keys():
            self.assertEqual(result[key], self.searchOutputStringExample[key])

    def test_that_verifies_output_values_of_float_attribute_search_match_when_no_match_occurs(self):

        demoHeader = PyMincHeader('demo/demo.mnc')
        result = demoHeader.search(self.nonExistingAttribute)

        for key in result.keys():
            self.assertEqual(result[key], self.searchOutputNonExistingExample[key])
