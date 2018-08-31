# https://github.com/Droogans/unmaintainable-code

import re
import os
import sys
import random

# TODO: Arrays: char name[5] = "Kike";
# TODO: Concat-vars: int num, counter = 0;
# FIXME: Vars in text = int var; char* txt = "var is awesome";

class Main:
  
  def __init__(self, argv):
    self.vars = []
    self.path = os.path.join(os.getcwd(), argv[1])
    self.ext  = self.path.split('.').pop()
    self.out  = self.path + '.' + self.ext # FIXME: Better rename or sustitution

    self.__lang__(self.ext)


  def __lang__(self, ext):
    if ext.lower() == 'c':
      self.avoid    = [
        'main'
      ]
      self.vartype  = [
        'char', 'int', 'short', 'long', 'float', 'double'
      ]


  def fileMgmt(self):
    with open(self.path, 'r') as _file, open(self.out, 'w') as _output:
      self.code = _file.read()
      for line in self.code.split('\n'):
        line = self.regex(line)
        self.findvars(line)
      self.vars.sort()
      self.naming_underscore()
      self.naming_singleletter()
      if self.ext.lower() == 'c':
        self.camouflage_lookbusy()
        self.misc_reversetruefalse()

      _output.write(self.code)


  def regex(self, line):
    fline = re.sub('[\ \(\)\,\;]', '¬', line)                     # Replace 'spaces ( ) , ;' with '¬'
    fline = re.sub('(["\'])(?:(?=(\\\?))\\2.)*?\\1', '¬', fline)  # Replace text strings with '¬'
    fline = re.sub('¬{2,}', '¬', fline)                           # Replace repeated '¬' with one
    fline = re.sub('(^¬|¬$)', '', fline)                          # Erase '¬' in the beginnig and the end of the line
    return fline


  def findvars(self, line):
    i = 0
    sline = line.split('¬')
    while i < len(sline) - 1:
      if sline[i] in self.vartype:
        if not sline[i+1] in self.avoid:
          self.vars.append(sline[i+1])
          i += 1
      i += 1


  def naming_underscore(self, quantity='2'):
    underscore = ''
    for x in range(quantity):
      underscore += '_'
      self.code = re.sub('\\b{}\\b'.format(random.choice(self.vars)), underscore, self.code)

  
  def naming_singleletter(self):
    i = 0
    singleletter = [ '`' ]
    while i < len(self.vars):
      if singleletter[-1] == 'z':
        j = -1
        while j > -len(singleletter) - 1 and singleletter[j] == 'z':
          singleletter[j] = 'a'
          j -= 1
        if j == -len(singleletter) - 1:
          singleletter.insert(0, 'a')
        else:
          singleletter[j] = chr(ord(singleletter[j]) + 1)
      else:
        singleletter[-1] = chr(ord(singleletter[-1]) + 1)

      self.code = re.sub('\\b{}\\b'.format(self.vars[i]), ''.join(singleletter), self.code)
      i += 1


  def naming_underscore(self, quantity=2):
    underscore = ''
    for x in range(quantity):
      underscore += '_'
      self.code = re.sub('\\b{}\\b'.format(random.choice(self.vars)), underscore, self.code)

  
  def camouflage_lookbusy(self):
    definitions = [
      [
        'cloneit(x,y,z)',
        'add_two(x,y)',
        'check(in, out)',
        'distance_between(d1, d2)',
        'fastcopy(x, y, out)',
      ],
      [
        '/* super useful */',
        '/* love it */',
        '/* thanx stackoverflow! */',
        '/* x, y, z */',
        '/* better define */',
        '/* only works with this */',
        '/* thanx */',
        '/* don\'t delete this */',
        '/* another guy wrote this, but work */',
        '/* TODO: Implement more functions */',
      ]
    ]

    # TODO: Include definitions inside the code: fastcopy(x,y,z);

    self.code = '\n' + self.code
    for definition in definitions[0]:
      self.code = '#define {0} {1}\n'.format(definition, random.choice(definitions[1])) + self.code


  def misc_reversetruefalse(self):
    self.code = '#define FALSE 1\n\n' + self.code
    self.code = '#define TRUE 0\n' + self.code

    self.code = re.sub('\\btrue\\b', 'FALSE', self.code)
    self.code = re.sub('\\bfalse\\b', 'TRUE', self.code)


  def run(self):
    self.fileMgmt()



if __name__ == '__main__':
  if (len(sys.argv) != 2): # FIXME: Better error
    print("Must have an argument")
    sys.exit(0)

  main = Main(sys.argv)
  main.run()