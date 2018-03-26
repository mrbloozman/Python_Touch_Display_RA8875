# import sys
# sys.path.append('../touch_display_ra8875')
# from __init__ import *
# from touch_display_ra8875 import *
from touch_display_ra8875_sim import *

RA8875_INT = 'XIO-P1'
RA8875_CS = 'XIO-P2'
RA8875_RESET = 'XIO-P3'

tft = Adafruit_RA8875(RA8875_CS, RA8875_RESET)

# /* Initialise the display using 'RA8875_480x272' or 'RA8875_800x480' */
if not tft.begin(RA8875sizes.RA8875_800x480):
	try:
		Exception("RA8875 Not Found!")
	except Exception as e:
		raise e

print("Found RA8875")

tft.displayOn(True)
tft.GPIOX(True)      # Enable TFT - display enable tied to GPIOX
tft.PWM1config(True, RA8875_PWM_CLK_DIV1024) # PWM output for backlight
tft.PWM1out(255)

td = TouchDisplay(
	# required args
	intPin='XIO-P#',
	tft=tft
	)

screen0 = Screen(
	# required args
	id=0,
	parent=td,
	# options
	fg_color=0xFFFF,
	bg_color=0x0000
	)

label0 = Label(
	parent=screen0,
	size=2,
	text='Test Label0',
	border=1
)

label0.center()
label0.middle()

print(vars(label0))

screen1 = Screen(
	id=1,
	parent=td
	)

screen2 = Screen(
	id=2,
	parent=td
	)

td.status(screen=0)
td.run(handleInterrupt=True,handleUpdate=True)

