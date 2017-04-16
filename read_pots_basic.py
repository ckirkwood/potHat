# Print the output of 3 pots - follow Adafruit tutorial for wiring

import time
import Adafruit_MCP3008

# Software SPI setup
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

values = [0]*3
for i in range(3):
	values[i] = mcp.read_adc(i)

while True:
	pot1 = mcp.read_adc(0)
	pot2 = mcp.read_adc(1)
	pot3 = mcp.read_adc(2)
	print(pot1, pot2, pot3)
	time.sleep(0.5)


# Print values inside a string
#while True:
#	values = [0]*3 # number of inputs
#	for i in range(3):
#		values[i] = mcp.read_adc(i)
#	print('Red Pot = {0}, Green Pot = {1}, Blue Pot = {2}'.format(*values))
#	time.sleep(0.5)

