"""
 -- UnmaintableCode: C Module --
 Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""
# pylint: disable=too-few-public-methods, no-self-use, unused-argument, dangerous-default-value

import re

class Module:
    """ Redefine True/False Convention """
    def __init__(self, variables):
        self.head = ''

    def run_(self, code, args={}):
        """ Define True as 0 and False as 1 """
        self.head = '#define TRUE 0\n'
        self.head += '#define FALSE 1\n'
        code = re.sub('\\btrue\\b', 'FALSE', code)
        code = re.sub('\\bfalse\\b', 'TRUE', code)
        return self.head, code
