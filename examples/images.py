import sys
sys.path.append('../touch_display_ra8875')
from __init__ import *
from adafruit_ra8875 import *
from netpbm import *
import CHIP_IO.GPIO as GPIO
import CHIP_IO.OverlayManager as OM

OM.load('SPI2')

RA8875_INT = 'XIO-P1'
RA8875_CS = 'XIO-P2'
RA8875_RESET = 'XIO-P3'

tft = Adafruit_RA8875(RA8875_CS, RA8875_RESET)

if not tft.begin(RA8875sizes.RA8875_800x480):
	print "RA8875 Not Found!"
	raise

tft.displayOn(True)
tft.GPIOX(True)      # Enable TFT - display enable tied to GPIOX
tft.PWM1config(True, RA8875_PWM_CLK_DIV1024) # PWM output for backlight
tft.PWM1out(255)
tft.touchEnable(True)

GPIO.setup(RA8875_INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = TouchDisplay(intPin=RA8875_INT,tft=tft)

screen = Screen(
	id=0,
	parent=app,
	fg_color=RA8875_YELLOW,
	bg_color=RA8875_RED
	)

pbm = NetPBM()
pbm.load('P1.pbm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center(150)
img.middle(150)

pbm = NetPBM()
pbm.load('P2.pgm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center()
img.middle(150)

pbm = NetPBM()
pbm.load('P3.ppm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center(650)
img.middle(150)

pbm = NetPBM()
pbm.load('P4.pbm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center(150)
img.middle(350)

pbm = NetPBM()
pbm.load('P5.pgm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center()
img.middle(350)

pbm = NetPBM()
pbm.load('P6.ppm')
img = Image(
	parent=screen,
	border=0,
	w=pbm.width(),
	h=pbm.height(),
	src=pbm.export(ColorMap.b16)
	)
img.center(650)
img.middle(350)

# grid = Grid(
# 	parent=screen,
# 	rows=2,
# 	cols=3,
# 	h=tft.height(),
# 	w=tft.width()
# 	)

# for imgfile in ['P1.pbm','P2.pgm','P3.ppm','P4.pbm','P5.pgm','P6.ppm']:
# 	pbm = NetPBM()
# 	pbm.load(imgfile)

# 	img = Image(
# 		parent=grid,
# 		border=0,
# 		w=pbm.width(),
# 		h=pbm.height(),
# 		src=pbm.export(ColorMap.b16)
# 		)

# grid.position()

screen.active(True)