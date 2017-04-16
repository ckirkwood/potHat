## Assign GPIO pins to MCP3008 ADC

import time
import Adafruit_MCP3008

CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
