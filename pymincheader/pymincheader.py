import os
import subprocess

class PyMincHeader():

    def __init__(self,fileName):

        if not os.path.isfile(fileName):
            raise Exception('PyMincHeader.__init__(): ' + fileName + ' does not exist')
        else:
            self.fileName = fileName
