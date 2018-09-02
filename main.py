"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
Inspiration: How To Write Unmaintainable Code (https://github.com/Droogans/unmaintainable-code)
"""
import os
import re
import sys

class Flow:
    """ Program behaviour """
    def __init__(self, filename):
        # Set source-code configuration
        self.source = {
            'code': None,
            'rcode': None,
            'variables': [],

            'path': os.path.abspath(filename)
        }

        # Set program configuration
        self.config = {
            'lang': {
                'blacklist': None,
                'var_types': None,

                'ext': self.source['path'].split('.').pop()
            },

            'mods': {},
            'current_mods': [],
            'mods_dir': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')
        }


    def import_(self):
        """ Import of necessary functions and variables depending on the extension """
        # Modify the PATH to be able to import modules
        if not self.config['mods_dir'] in sys.path:
            sys.path.append(self.config['mods_dir'])
        # Import variable type names
        try:
            self.config['lang']['blacklist'] = __import__(self.config['lang']['ext'] + '_lang').blacklist
            self.config['lang']['var_types'] = __import__(self.config['lang']['ext'] + '_lang').variables
        # FIXME: Better errors
        except ImportError:
            sys.exit('Modules not found')
        except AttributeError:
            sys.exit('Incomplete modules')
        # Find all the available modules
        for module in os.listdir(self.config['mods_dir']):
            if module.startswith(self.config['lang']['ext']) and not module.endswith('_lang.py'):
                self.config['current_mods'].append(module)
        
        print(self.config)


    def read_(self):
        """ Read the source code from the file """
        with open(self.source['path'], 'r') as source:
            self.source['code'] = source.read().strip()


    def clean_(self):
        """ Clean the code of characters that do not provide information """
        # Replace =, (, ), \" and ; with spaces
        self.source['rcode'] = re.sub('([\\*;=()]|\\\\")', ' ', self.source['code'])
        # Replaces array sizes or index with spaces
        self.source['rcode'] = re.sub('\[[0-9]*\]', ' ', self.source['rcode'])
        # Separate the " to better visualize the strings
        self.source['rcode'] = re.sub('"', ' " ', self.source['rcode'])
        # Replace two or more spaces with one space
        self.source['rcode'] = re.sub('\\ {2,}', ' ', self.source['rcode'])
        # Remove blank lines and spaces in the beggining of the line
        self.source['rcode'] = re.sub('(^\\ |^\n)', '', self.source['rcode'], flags=re.MULTILINE)


    def analize_(self):
        """ Analysis of the source code to search for variables """
        # FLAG: Variable name found!
        var_found = False
        # FLAG: Is part of a string or not
        in_string = False
        # Read the file word by word
        for line in self.source['rcode'].split('\n'):
            for word in line.split(' '):
                if word == '"':
                    in_string = not in_string
                elif not in_string and word in self.config['lang']['var_types']:
                    var_found = True
                elif var_found and word not in self.config['lang']['blacklist']:
                    var_found = False
                    self.source['variables'].append(word)


if __name__ == '__main__':
    # Check if there are arguments
    if len(sys.argv) != 2:
        # FIXME: Better error msg
        # TODO: Two or more files at once
        sys.exit('You must specify the name of the file')
    else:
        FLOW = Flow(sys.argv[1])
        FLOW.import_()
        FLOW.read_()
        FLOW.clean_()
        FLOW.analize_()
