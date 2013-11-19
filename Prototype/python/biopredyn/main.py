## @package biopredyn
## @author: $Author$
## @date: $Date$
## @copyright: $Copyright: [2013] BioPreDyn $
## @version: $Revision$

import sys
import os

# Find the path to the libsedml Python package
for r, d, f in os.walk(os.path.join(os.path.dirname(__file__), '../../bin')):
  for filename in f:
    if filename == "libsedml.py":
      sys.path.append(os.path.abspath(r))
      break

# Find the path to the libsbmlsim Python package
for r, d, f in os.walk(os.path.join(os.path.dirname(__file__), '../../bin')):
  for filename in f:
    if filename == "libsbmlsim.py":
      sys.path.append(os.path.abspath(r))
      break

# Find the path to the libnuml Python package
for r, d, f in os.walk(os.path.join(os.path.dirname(__file__), '../../bin')):
  for filename in f:
    if filename == "libnuml.py":
      sys.path.append(os.path.abspath(r))
      break

import getopt
import sys
import textwrap
import numpy as np
import matplotlib.pyplot as plt

import libsbml
import libsedml
import libnuml
import model
import workflow

COMMAND_SYNTAX_MESSAGE = 'python main.py /path/to/input/file [options]'

HELP_MESSAGE = "This program is a prototype for the BioPreDyn software suite developed within the scope of the BioPreDyn FP7 project; it applies an analysis pattern to an SBML model defining a biological system."

# Optional parameters.
HELP_OPTION = {
"help"    : [  "Display this help message."],
"cobra"   : [  "Open the input file using the cobrapy library."],
"copasi"  : [  "Open the input SED-ML file and execute its tasks using the Copasi library."],
"sbml"    : [  "Open the input file as an SBML model; SBML compliance will be checked."],
"sedml"   : [  "Open the input SED-ML model file and execute its tasks using the libSBMLSim library."],
}

HELP_KEYWORD_SIZE = 16   # Left column
HELP_WRAP_SIZE = 79   # Total. 79 is windows limit

## Display help information.
def print_help():
  # General help message
  print " "
  lines = textwrap.wrap(HELP_MESSAGE, HELP_WRAP_SIZE)
  for line in lines:
    print line
  print " "
  
  # Command syntax
  print "Usage: "
  print (COMMAND_SYNTAX_MESSAGE)
  print " "
  print "List of available options: "
  
  # Optional arguments
  for arg in HELP_OPTION:
    print_help_argument(arg, HELP_OPTION[arg])

## Display help information for the input option.
# @param arg Name of the help option to be displayed.
# @param listhelplines Information about the help option being displayed.
def print_help_argument(arg, listhelplines):
  firstLine = True
  # Go trough list of help line
  for helpline in listhelplines:
    lines = textwrap.wrap(helpline, HELP_WRAP_SIZE - HELP_KEYWORD_SIZE)
    for line in lines:
      # First line: Print arg name.
      if firstLine:
        print ('--' + arg).ljust(HELP_KEYWORD_SIZE) + line
        firstLine = False
      else:
        print ''.ljust(HELP_KEYWORD_SIZE) + line
  print ""

# main
try:
  opts, args = getopt.getopt(sys.argv[2:], "", [
      'help', 'cobra', 'copasi', 'sbml', 'sedml'])
except getopt.error, msg:
  print( COMMAND_SYNTAX_MESSAGE )
  print( "Type main.py --help for more information" )
  print( msg )
  sys.exit(2)

for o, a in opts:
  print str(o)
  if o == "--help":
    print_help()
    sys.exit(0)
  elif o == "--sbml":
    model = model.SBMLModel(sys.argv[1])
    model.check()
  elif o == "--sedml":
    flow = workflow.WorkFlow(sys.argv[1])
    flow.run_tasks()
  elif o == "--cobra":
    print("Something will happen with cobrapy here soon.")
  elif o == "--copasi":
    # TODO: run and plot methods are not defined in Workflow class anymore
    flow = workflow.WorkFlow(sys.argv[1])
    flow.run()
    flow.plot()