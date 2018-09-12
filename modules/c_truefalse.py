"""
 -- UnmaintableCode: C Module --
 Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""
# pylint: disable=too-few-public-methods, no-self-use, unused-argument, dangerous-default-value

import re

class Module:
    """ Redefine True/False Convention """
    def __init__(self, variables):
        pass

    def run_(self, code, args={}):
        """ Define True as 0 and False as 1 """
        code = '#define FALSE 1\n\n' + code
        code = '#define TRUE 0\n' + code
        code = re.sub('\\btrue\\b', 'FALSE', code)
        code = re.sub('\\bfalse\\b', 'TRUE', code)
        return code
