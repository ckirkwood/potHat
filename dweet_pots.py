## Send analogue values to Dweet.io

################################################################################    
#    Copyright © 2017 Callum Kirkwood                                          #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
################################################################################

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
