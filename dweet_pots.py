## Send output from pots to Dweet.io

import dweepy
import Adafruit_MCP3008
import time

## Software SPI setup
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


## Convert 10-bit ADC output to RGB friendly 0-255, store as variables
## NewValue = (((OldValue - OldMin) * (NewMax - NewMin) / (OldMax - OldMin)) + $

while True:
        red = (((mcp.read_adc(0) - 0) * (255 - 0)) / (1023 - 0)) + 0
        blue  = (((mcp.read_adc(2) - 0) * (255 - 0)) / (1023 - 0)) + 0
        green = (((mcp.read_adc(1) - 0) * (255 - 0)) / (1023 - 0)) + 0
	dweepy.dweet_for('pot-one', {'red': red})
	time.sleep(0.1)
	dweepy.dweet_for('pot-two', {'blue': blue})
	time.sleep(0.1)
	dweepy.dweet_for('pot-three', {'green': green})
	time.sleep(0.2)
