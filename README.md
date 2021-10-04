# Package documentation of <code>org.slashlib.py.argument</code>  

<code>@Argument</code> hides pythons <code>argparse</code> magic behind a fancy decorator
and helps reducing boilerplate code, by instrumenting python properties and type hints.

## content ##

* Usage
  * [Getting started guide (see 'getting started' below)](#getting-started)
* Developers
  * [API](docs/markdown/index.md)
  * [Frameworks used for building, testing, etc.](docs/frameworks.md)

## getting started ##

### prerequisites ###

<p>This project requires python 3.9 or newer and upgrading pip and setuptools.</p>
<code>python -m pip install --upgrade pip</code><br />
<code>pip install --upgrade setuptools</code>

### install ###

<code>pip install org.slashlib.py.argument</code>

## usage ##


```python
# file test.py
from typing                     import Optional
from org.slashlib.py.argument   import Argument

class MyArguments:
   def __init__( self ):
       self._filename = None

   @Argument
   @property
   def filename( self ) -> Optional[ str ]:
       """ Some fancy filename """
       return self._filename

if __name__ == "__main__":
   import org.slashlib.py.argument.parser as parser
   parser.getInstance( description = "Run a simple script" ).parse()

   myargs = MyArguments()
   print( myargs.filename )


# (python39) PS > python test.py -h
# usage: test.py [-h] [-f FILENAME]
#
# Run a simple script
#
# optional arguments:
#   -h, --help            show this help message and exit
#
#   -f FILENAME, --filename FILENAME
#                         Some fancy filename
#
# (python39) PS > python test.py -f "blubb"
# blubb
# (python39) PS > python test.py --filename "blubb"
# blubb
#
# # Error in next call: missing '-' in argument '-filename':
# (python39) PS > python test.py -filename "blubb"
# usage: test.py [-h] [-f FILENAME]
# test.py: error: unrecognized arguments: blubb
```
