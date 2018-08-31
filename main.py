# https://github.com/Droogans/unmaintainable-code
import re
import os
import sys

class Main:
  

  def __init__(self, argv):
    self.vars = []
    self.path = os.path.join(os.getcwd(), argv[1])
    self.out  = self.path + '.uc' # FIXME: Better rename or sustitution
    self.ext  = self.path.split('.').pop()

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
      self.singleLetter()

      _output.write(self.code)

  def regex(self, line):
    fline = re.sub('[\ \(\)\,\;]', '¬', line) # Replace 'spaces ( ) , ;' with '¬'
    fline = re.sub('¬{2,}', '¬', fline)     # Replace repeated '¬' with one
    fline = re.sub('(^¬|¬$)', '', fline)    # Erase '¬' in the beginnig and the end of the line
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

  
  def singleLetter(self):
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
  
  def run(self):
    self.fileMgmt()



if __name__ == '__main__':
  if (len(sys.argv) != 2): # FIXME: Better error
    print("Must have an argument")
    sys.exit(0)

  main = Main(sys.argv)
  main.run()