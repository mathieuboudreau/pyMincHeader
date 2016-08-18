import os
import subprocess
import re

class PyMincHeader():
    '''PyMincHeader: Class to fetch and hold mincheader information.

    --args--
        filename: string containing full filename of minc file

    --methods--
        search: parses header of minc file for a single occurence of headerAttribute

            --args--
                headerAttribute: string of an attribute-of-interest from the header file
                                **must only have a single occurance, be as exact as possible**

                                e.g. for the line: \n\t\tacquisition:flip_angle = 9. ;\n
                                     angle, flip_angle, or acquisition:flip_angle would be appropriate,
                                     but acquisition:flip_angle would be best since angle and flip_angle
                                     may have multiple occurances.

            --return--
                type: dict
                    format: {'attribute': self.attribute, 'value':self.value, 'line':self.matchedLine}
    '''

    def __init__(self,fileName):
        if not os.path.isfile(fileName):
            raise Exception('PyMincHeader.__init__(): ' + fileName + ' does not exist')
        else:
            self.fileName    = fileName
            self.headerCache = None
            self.__resetobj()

    def search(self, headerAttribute):
        '''PyMincHeader.search: parses header of minc file for a single occurence of headerAttribute

        --args--
            headerAttribute: string of an attribute-of-interest from the header file
                             **must only have a single occurance, be as exact as possible**

                             e.g. for the line: \n\t\tacquisition:flip_angle = 9. ;\n
                             angle, flip_angle, or acquisition:flip_angle would be appropriate,
                             but acquisition:flip_angle would be best since angle and flip_angle
                             may have multiple occurances.

        --return--
             type: dict
                 format: {'attribute': self.attribute, 'value':self.value, 'line':self.matchedLine}
        '''

        if not self.headerCache:
            # Need the with-as to avoid ResourceWarning: unclosed file [...] warning
            with subprocess.Popen(['mincheader', self.fileName],stdout=subprocess.PIPE) as terminalOutput:
                self.headerCache = terminalOutput.stdout.read()

        m = re.search(r'\n.*' + re.escape(headerAttribute) + '.*\n',str(self.headerCache,'utf-8'))

        # If no match is found, m should be None
        if m:
            self.headerAttribute = headerAttribute
            m = re.search(r'[[a-z]]*.*;', m.group()) # Remove escape characters of line
            self.matchedLine = m.group()

            # Fetch value
            m = re.search(r'= .* ', self.matchedLine)
            matchedValueString = m.group()
            self.stringValue = matchedValueString[2:-1] # Set member variable so that user can access and convert themselves
                                                        # if they want to.
                                                        #
                                                        # 2 -> "= ", -1 -> " "
            # Convert matched string value to appropriate type
            self.__convertValueStringToType()

            # Fetch full attribute name
            m = re.search(r'\w*:\w*', self.matchedLine)
            # If no match is found, m should be None
            if m:
                matchedAttributeString = m.group()
                self.attribute = matchedAttributeString
            else:
                m = re.search(r'\w*', self.matchedLine)
                matchedAttributeString = m.group()
                self.attribute = matchedAttributeString

        else:
            self.__resetobj()

        return {'attribute': self.attribute, 'value': self.value, 'line': self.matchedLine}

    def __resetobj(self):
        self.headerAttribute = None
        self.matchedLine     = None
        self.stringValue     = None
        self.value           = None
        self.attribute       = None

    def __convertValueStringToType(self):
        try:
            float(self.stringValue)
        except:
            self.value = self.stringValue[1:-1]
        else:
            self.value = float(self.stringValue)
