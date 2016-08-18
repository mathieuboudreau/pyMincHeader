import unittest
import subprocess

class MincEnvironmentTest(unittest.TestCase):
    ''' MINC Environment Test
    Test Class to verify MINC tool is installed and working as expected
    '''
    def setUp(self):
        self.expectedMincHeaderOutput = 'Usage: mincheader [-data] <minc file>\n' # True for libminc: 2.3.1
        pass

    def tearDown(self):
        pass

    def test_that_verifies_if_mincheader_tool_is_callable(self):
         self.actualMincHeaderOutput = subprocess.getoutput(['mincheader'])

         self.assertEqual(self.expectedMincHeaderOutput, self.actualMincHeaderOutput)
