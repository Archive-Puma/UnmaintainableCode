import re

class Module:
    def __init__(self, variables):
        pass

    def run_(self, code, args={'n': 3}):
        code = '#define FALSE 1\n\n' + code
        code = '#define TRUE 0\n' + code
        
        code = re.sub('\\btrue\\b', 'FALSE', code)
        code = re.sub('\\bfalse\\b', 'TRUE', code)
        return code
