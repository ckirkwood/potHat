import Adafruit_MCP3008
import blinkt
import time

## Software SPI setup
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

blinkt.set_brightness(0.2)


## Convert 10-bit ADC output to RGB friendly 0-255, store as variables
## NewValue = (((OldValue - OldMin) * (NewMax - NewMin) / (OldMax - OldMin)) + NewMin

while True:
	r = (((mcp.read_adc(0) - 0) * (7 - 0)) / (1023 - 0)) + 0
	g  = (((mcp.read_adc(1) - 0) * (7 - 0)) / (1023 - 0)) + 0
	scan = (((mcp.read_adc(2) - 0) * (7 - 0)) / (1023 - 0)) + 0
	blinkt.clear()
	blinkt.set_pixel(scan, r, g, 0)
	blinkt.show()


