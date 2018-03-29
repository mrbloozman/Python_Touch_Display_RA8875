# import sys
# sys.path.append('../touch_display_ra8875')
# from __init__ import *
# from touch_display_ra8875 import *
from touch_display_ra8875_sim import *

# Debug
def debug(obj):
	for k in vars(obj):
		v = vars(obj)[k]
		print(k+': '+str(v))

# Setup RA8875
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
tft.GPIOX(True)  # Enable TFT - display enable tied to GPIOX
tft.PWM1config(True, RA8875_PWM_CLK_DIV1024)  # PWM output for backlight
tft.PWM1out(255)

# Touch Display
td = TouchDisplay(
	# required args
	intPin='XIO-P#',
	tft=tft
)

# Define Screens
screen0 = Screen(
	# required args
	id=0,
	parent=td,
	# options
	fg_color=RA8875_YELLOW,
	bg_color=RA8875_BLACK
)

screen1 = Screen(
	id=1,
	parent=td,
	fg_color=RA8875_WHITE,
	bg_color=RA8875_RED
)

screen2 = Screen(
	id=2,
	parent=td,
	fg_color=RA8875_YELLOW,
	bg_color=RA8875_BLUE
)

screen3 = Screen(
	id=3,
	parent=td,
	fg_color=0x8090,
	bg_color=0xFFFF
)

screen4 = Screen(
	id=4,
	parent=td,
	fg_color=0xFFFF,
	bg_color=0x0000
)

# Define screen0 controls

label0 = Label(
	parent=screen0,
	size=2,
	text='Screen0'
)

btn0 = Button(
	parent=screen0,
	size=1,
	padding=20,
	text='Goto Screen1',
	onTap=screen1.active,
	onTapArgs=[True]
)

# Then position the screen0 controls
label0.center()
label0.middle()

btn0.center()
btn0.middle(350)

# Define screen1 controls
label1 = Label(
	parent=screen1,
	size=2,
	text='Screen1'
)

grid1 = Grid(
	parent=screen1,
	border=2,
	w=750,
	h=300,
	rows=2,
	cols=3
)

btn1a = Button(
	parent=grid1,
	size=1,
	text='Toggle Enable',
	onTap=screen2.active,
	onTapArgs=[True]
)

btn1b = Button(
	parent=grid1,
	size=1,
	text='Spinbox',
	onTap=screen3.active,
	onTapArgs=[True]
)

btn1c = Button(
	parent=grid1,
	size=1,
	text='Listbox',
	onTap=screen4.active,
	onTapArgs=[True]
)

label1d = Label(
	parent=grid1,
	size=1,
	text='Label 1d'
)
label1e = Label(
	parent=grid1,
	size=1,
	text='Label 1e'
)
label1f = Label(
	parent=grid1,
	size=1,
	text='Label 1f'
)

btn1 = Button(
	parent=screen1,
	size=1,
	padding=20,
	text='Goto Screen0',
	onTap=screen0.active,
	onTapArgs=[True]
)

# Then position the screen1 controls
label1.center()
label1.top()

grid1.center()
grid1.middle()

btn1.center()
btn1.bottom()

# Define screen2 controls
label2 = Label(
	parent=screen2,
	size=2,
	text='Screen 2'
)

lbl_input2 = Label(
	parent=screen2,
	size=1,
	text='Input Control: '
)

input2 = Input(
	parent=screen2,
	size=1,
	datatype=t_datatype.text,
	value='Black when disabled',
	enabled=False
)

toggle2 = Toggle(
	parent=screen2,
	size=1,
	text='Input Enabled Toggle',
	onSelect=input2.enabled,
	onSelectArgs=['_selected']
)

# position screen2
label2.center()
label2.top()

lbl_input2.middle()
lbl_input2.right(400)

input2.middle()
input2.left(400)

toggle2.center()
toggle2.bottom()

# screen3 controls
label3 = Label(
	parent=screen3,
	size=1,
	text='Screen 3'
)

sbox3 = Spinbox(
	parent=screen3,
	size=3,
	border=2,
	text='Spin: ',
	value=5,
	mn=0,
	mx=10
)

label3.left()
label3.top()

sbox3.middle()
sbox3.center()

# screen4 controls
lbl4 = Label(
	parent=screen4,
	text='Screen 4',
	size=1
)

lbl_lbox4 = Label(
	parent=screen4,
	text='Select BG Color: ',
	size=1
)

lbox4 = Listbox(
	parent=screen4,
	rows=3,
	value=0,
	w=400,
	h=300,
	onChange=screen4.bg_color,
	onChangeArgs=['_value'],
	onTap=screen4.active,
	onTapArgs=[True]
)

item1 = ListboxItem(
	parent=lbox4,
	size=1,
	text='Red',
	value=RA8875_RED
)

item2 = ListboxItem(
	parent=lbox4,
	size=1,
	text='Green',
	value=RA8875_GREEN
)

item3 = ListboxItem(
	parent=lbox4,
	size=1,
	text='Blue',
	value=RA8875_BLUE
)

lbl4.center()
lbl4.top()

lbl_lbox4.middle()
lbl_lbox4.center(250)

lbox4.middle()
lbox4.center(650)





# put a control on all screens except screen0
btn_exit = Button(
	parent=screen1,
	size=1,
	text='EXIT',
	onTap=screen0.active,
	onTapArgs=[True]
)

btn_exit.top()
btn_exit.right()

for s in td.screens():
	if s.id() != 0:
		s.addControl(btn_exit)

# Set the starting screen id, then run the touch display
td.setScreen(0)
td.run(handleInterrupt=True, handleUpdate=True)
