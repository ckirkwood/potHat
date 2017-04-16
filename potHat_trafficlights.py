## Control LEDs connected to GPIO pins 6, 12 & 13 (with a button on 19)

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

