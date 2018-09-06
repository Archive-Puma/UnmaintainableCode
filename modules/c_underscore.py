import re
from random import randint

class Module:
    def __init__(self, variables):
        self.variables = variables

    def run_(self, code, args={'n': 3}):
        for i in range(args['n']):
            changed = self.variables[randint(0, len(self.variables) - 1)]
            code = re.sub('\\b{}\\b'.format(changed), '_' * (i + 1), code)
        return code
