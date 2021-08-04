#
# User defined tasks setup.
# Generated from buildmytask.
#

import sys
from casa_stack_manip import stack_frame_find

if sys.path[1] != '/home/marti/WORKAREA/GITHUB/PolConvert':
  sys.path.insert(1, '/home/marti/WORKAREA/GITHUB/PolConvert')
from odict import odict
if not globals().has_key('mytasks') :
  mytasks = odict()

mytasks['polconvert'] = '\n\nVersion 1.9.0 -- Converts VLBI visibilities polarization basis.'

if not globals().has_key('task_location') :
  task_location = odict()

task_location['polconvert'] = '/home/marti/WORKAREA/GITHUB/PolConvert'
myglobals = stack_frame_find( )
tasksum = myglobals['tasksum'] 
for key in mytasks.keys() :
  tasksum[key] = mytasks[key]

from polconvert_cli import  polconvert_cli as polconvert
