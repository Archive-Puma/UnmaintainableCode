"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
Inspiration: How To Write Unmaintainable Code (https://github.com/Droogans/unmaintainable-code)
"""
import os
import re
import sys
import errno

class Flow:
    """ Program behaviour """
    def __init__(self, filename):
        # Set source-code configuration
        self.source = {
            'code': str(),
            'head': str(),
            'rcode': str(),
            'variables': list(),
            'filename': os.path.basename(filename),
            'path': os.path.abspath(filename)
        }

        # Set program configuration
        self.config = {
            'lang': {
                'blacklist': list(),
                'var_types': list(),

                'ext': self.source['path'].split('.').pop()
            },

            'mods': {},
            'lang_dir': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lang'),
            'mods_dir': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')
        }


    def import_(self):
        """ Import of necessary functions and variables depending on the extension """
        # Modify the PATH to be able to import modules and languages
        if not self.config['mods_dir'] in sys.path:
            sys.path.append(self.config['mods_dir'])
        if not self.config['lang_dir'] in sys.path:
            sys.path.append(self.config['lang_dir'])
        # Import variable type names
        try:
            self.config['lang']['blacklist'] = \
                __import__('lang_' + self.config['lang']['ext']).BLACKLIST
            self.config['lang']['var_types'] = \
                __import__('lang_' + self.config['lang']['ext']).VARIABLES
        # FIXME: Better errors
        except ImportError:
            sys.exit('Modules not found')
        except AttributeError:
            sys.exit('Incomplete modules')
        # Find all the available modules
        for module in os.listdir(self.config['mods_dir']):
            # Check current language and python extension
            if module.startswith(self.config['lang']['ext']) and module[-3:] == '.py':
                # Format name: extension
                module = module[:-3]
                self.config['mods'][module[len(self.config['lang']['ext']) + 1:]] = \
                    __import__(module).Module(self.source['variables'])


    def read_(self):
        """ Read the source code from the file """
        with open(self.source['path'], 'r') as source:
            self.source['code'] = source.read().strip()


    def clean_(self):
        """ Clean the code of characters that do not provide information """
        # Replace =, (, ), \" and ; with spaces
        self.source['rcode'] = re.sub('([\\*;=()]|\\\\")', ' ', self.source['code'])
        # Replaces array sizes or index with spaces
        self.source['rcode'] = re.sub('\\[[0-9]*\\]', ' ', self.source['rcode'])
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


    def run_modules_(self):
        """ Run the available modules """
        # Split includes and defines from the source code
        for _header in re.findall('^#.+', self.source['code'], flags=re.MULTILINE):
          self.source['head'] += _header + '\n'
        self.source['code'] = re.sub('^#.+', '', self.source['code'], flags=re.MULTILINE)
        self.source['code'] = re.sub('\n{2,}', '\n', self.source['code'])
        print(self.source['code'])
        for module in self.config['mods']:
            head, self.source['code'] = \
                self.config['mods'][module].run_(self.source['code'])
            if head != '':
                self.source['head'] += head + '\n'
        # Append head to the code
        self.source['code'] = self.source['head'] + self.source['code']


    def save_(self):
        """ Save the new and awesome source code in a file """
        output = os.path.join(os.getcwd(), 'output')
        if not os.path.exists(output):
            # Guard against Race Condition
            try:
                os.makedirs(output)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
        output = os.path.join(output, self.source['filename'])
        with open(output, 'w') as _output:
            _output.write(self.source['code'])


if __name__ == '__main__':
    # Check if there are arguments
    if len(sys.argv) != 2:
        # FIXME: Better error msg
        # TODO: Two or more files at once
        sys.exit('You must specify the name of the file')
    else:
        # Run the program flow
        FLOW = Flow(sys.argv[1])
        FLOW.import_()
        FLOW.read_()
        FLOW.clean_()
        FLOW.analize_()
        FLOW.run_modules_()
        FLOW.save_()
