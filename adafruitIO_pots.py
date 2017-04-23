# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony DiCola

# Import Adafruit IO REST client.
from Adafruit_IO import Client
import Adafruit_MCP3008
from time import sleep

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'API_KEY'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

## Software SPI setup for MCP3008
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

## Adjust the output range if necessary and send the values to an Adafruit IO Feed
## NewValue = (((OldValue - OldMin) * (NewMax - NewMin) / (OldMax - OldMin)) + $
while True:
        pot1 = (((mcp.read_adc(0) - 0) * (255 - 0)) / (1023 - 0)) + 0
        pot2 = (((mcp.read_adc(2) - 0) * (255 - 0)) / (1023 - 0)) + 0
        pot3 = (((mcp.read_adc(1) - 0) * (255 - 0)) / (1023 - 0)) + 0
	aio.send('pot-1', pot1)
	aio.send('pot-2', pot2)
	aio.send('pot-3', pot3)
	sleep(0.5)
