## Adjust the RGB values of Pimoroni's Blinkt using 3 pots

from gpiozero import LED, Button
import Adafruit_MCP3008
import blinkt
import time


## Software SPI setup
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

blinkt.set_brightness(0.5)

## Convert 10-bit ADC output to RGB friendly 0-255, store as variables
## NewValue = (((OldValue - OldMin) * (NewMax - NewMin) / (OldMax - OldMin)) + NewMin

while True:
	r = (((mcp.read_adc(0) - 0) * (255 - 0)) / (1023 - 0)) + 0
	g  = (((mcp.read_adc(1) - 0) * (255 - 0)) / (1023 - 0)) + 0
	b = (((mcp.read_adc(2) - 0) * (255 - 0)) / (1023 - 0)) + 0
	blinkt.clear()
	blinkt.set_all(r, g, b)
	blinkt.show()
	time.sleep(0.1)

