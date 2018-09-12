"""
 -- UnmaintableCode: C Module --
 Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""
# pylint: disable=too-few-public-methods, no-self-use, unused-argument, dangerous-default-value

import re

class Module:
    """ Convert numeric numbers to no-numeric numbers """
    def __init__(self, variables):
        self.head = ''
        self.prefix = 'NUM_'
        self.numbers = {
            '0': 'ZERO',
            '1': 'ONE',
            '2': 'TWO',
            '3': 'THREE',
            '4': 'FOUR',
            '5': 'FIVE',
            '6': 'SIX',
            '7': 'SEVEN',
            '8': 'EIGHT',
            '9': 'NINE',
            '10': 'TEN',
            '20': 'TWENTY',
            '30': 'THIRTY',
            '40': 'FOURTY',
            '50': 'FIFTY',
            '60': 'SIXTY',
            '70': 'SEVENTY',
            '80': 'EIGHTY',
            '90': 'NINETY',
            '100': 'ONE_HUNDRED',
            '1000': 'ONE_THOUSAND',
            '10000': 'TEN__THOUSAND',
            '100000': 'ONE_HUNDRED_THOUSAND',
            '1000000': 'ONE_MILLION',
            '-1': 'NEGATIVE_ONE'
        }

    def run_(self, code, args={}):
        """ Replace single numbers using their names """
        for key in self.numbers:
            number = self.prefix + self.numbers[key]
            self.head += '#define {0} {1}\n'.format(number, key)
            code = re.sub('\\b({})\\b'.format(key), number, code)
        return self.head, code
