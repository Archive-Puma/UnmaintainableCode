<img src=".repository/goodjob.png" align="right" width="150">

# Unmaintainable Code
![language](https://img.shields.io/badge/language-python%203-blue.svg?style=for-the-badge)

:vhs: Clone me!
----
Clone or download the project:
```sh
git clone https://github.com/cosasdepuma/unmaintainablecode.git UnmaintainableCode
  [ or ]
git clone https://gitlab.com/cosasdepuma/unmaintainablecode.git UnmaintainableCode

cd UnmaintainableCode
```

:electric_plug: Requirements
----
Unmaintainable Code does not require anything!


:runner: Usage
----
To turn your wonderful and well-developed code into a 💩 you only have to execute the following command:

```py
python main.py [path to your source code]
```


:package: Create your own modules!
----

Copy the template that is inside the `modules` folder and rename it using the following pattern:

```
[lang extension]_[module name].py
```

In this way, if we want to create a JavaScript module, the module could be called `js_myawesomemodule.py`.

All new modules must be based on the following template:

```py
"""
 -- UnmaintableCode: [Lang] Module --
 Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""
# pylint: disable=too-few-public-methods, no-self-use, unused-argument, dangerous-default-value

# imports go here

class Module:
    """ Class DocString: Simple explanation about the module  """
    def __init__(self, variables):
        self.head = ''
        # self.variables = variables

    def run_(self, code, args={}):
        """ Method DocString: Simple explanation about the algorithm """
        # your code goes here
        return self.head, code
```

Take a look at some examples in the `modules` folder.


:octopus: Support the developer!
----
Everything I do and publish can be used for free whenever I receive my corresponding merit.

Anyway, if you want to help me in a more direct way, you can leave me a tip by clicking on this badge:

<p align="center">
    </br>
    <a href="https://www.paypal.me/cosasdepuma/"><img src="https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge" alt="PayPal Donation"></img></a>
</p>


:earth_africa: Scheme of contents
----
```
Polyglot-Code
 < Repository >
|__ .gitignore
|__ .repository
  |__ goodjob.png
|__ LICENSE
|__ README.md
< Program >
|__ main.py
< Languages >
|__ lang
  |__ lang_c.py
< Modules >
|__ modules
  |__ template.py
  |__ c_nonumeric.py
  |__ c_truefalse.py
  |__ c_underscore.py
```

:memo: To Do
----

 - [ ] Choose a super amazing license
 - [ ] Create a PyPi packaged version
 - [ ] Don't replace variable names in strings!

----

Please contact with [Kike Puma](https://linkedin.com/in/kikepuma) if you need more information.
