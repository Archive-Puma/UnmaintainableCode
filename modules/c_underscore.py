"""
 -- UnmaintableCode: C Module --
 Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""
# pylint: disable=too-few-public-methods, no-self-use, unused-argument, dangerous-default-value

import re
from random import randint

class Module:
    """ Rename variables to _ or __ """
    def __init__(self, variables):
        self.head = ''
        self.variables = variables

    def run_(self, code, args={'n': 3}):
        """ n: Number of variables to rename """
        for i in range(args['n']):
            changed = self.variables[randint(0, len(self.variables) - 1)]
            code = re.sub('\\b{}\\b'.format(changed), '_' * (i + 1), code)
        return self.head, code
