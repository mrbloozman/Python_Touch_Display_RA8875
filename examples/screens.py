import sys
sys.path.append('../touch_display_ra8875')
from __init__ import *

td = TouchDisplay(
	# required args
	intPin='XIO-P#',
	tft='tftobj'
	)

screen0 = Screen(
	# required args
	id=0,
	parent=td,
	# options
	fg_color=0xFFFF,
	bg_color=0x0000
	)

screen1 = Screen(
	id=1,
	parent=td
	)

screen2 = Screen(
	id=2,
	parent=td
	)

td.status(screen=0)
td.run(handleUpdate=True)

