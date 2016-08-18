import os
import subprocess
import re

class PyMincHeader():

    def __init__(self,fileName):

        if not os.path.isfile(fileName):
            raise Exception('PyMincHeader.__init__(): ' + fileName + ' does not exist')
        else:
            self.fileName  = fileName
            self.headerCache     = None
            self.headerAttribute = None
            self.matchedLine     = None
            self.stringValue     = None
            self.value           = None
            self.attribute       = None

    def search(self, headerAttribute):

        if not self.headerCache:
            # Need the with-as to avoid ResourceWarning: unclosed file [...] warning
            with subprocess.Popen(['mincheader', self.fileName],stdout=subprocess.PIPE) as terminalOutput:
                self.headerCache = terminalOutput.stdout.read()

        m = re.search(r'\n.*' + re.escape(headerAttribute) + '.*\n',str(self.headerCache,'utf-8'))

        if m:
            self.headerAttribute    = headerAttribute
            m = re.search('[[a-z]]*.*;', m.group()) # Remove escape characters of line
            self.matchedLine = m.group()

            # Fetch value
            m = re.search(r'= .* ', self.matchedLine)
            matchedValueString = m.group()
            self.stringValue = matchedValueString[2:-1] # Set member variable so that user can access and convert themselves
                                                        # if they want to.
                                                        #
                                                        # 2 -> "= ", -1 -> " "
            self.value= float(self.stringValue)

            # Fetch full attribute name
            m = re.search(r'\w*:\w*', self.matchedLine)
            matchedAttributeString = m.group()
            self.attribute = matchedAttributeString

        else:
            self.headerAttribute = None
            self.matchedLine     = None
            self.stringValue     = None
            self.value           = None
            self.attribute       = None

        return {'attribute': self.attribute, 'value':self.value, 'line':self.matchedLine}
