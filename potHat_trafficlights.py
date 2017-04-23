## Control LEDs connected to GPIO pins 6, 12 & 13 (with a button on 19)
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

from gpiozero import LED, Button
from time import sleep

button = Button(19)
led_y = LED(6)
led_g = LED(12)
led_r = LED(13)


## Blink both LEDs simultaneously when button pressed
while True:
	button.wait_for_press()
	led_y.blink()
	sleep(1)
	led_g.blink()
	sleep(1)
	led_y.blink()

## Blink LEDs consecutively when button pressed
#while True:
#	button.wait_for_press()
#	led_g.on()
#	sleep(1)
#	led_g.off()
#	sleep(1)
#	led_r.on()
#	sleep(1)
#	led_r.off()
#	sleep(1)
#	led_y.on()
#	sleep(1)
#	led_y.off()
#	sleep(1)

