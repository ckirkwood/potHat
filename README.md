# potHat
#### Custom Raspberry Pi HAT with an ADC, 3 potentiometers and LEDs

Built as a solution to provide analogue inputs to the Raspberry Pi without the hassle of setting up a breadboard each time. The proto HAT also breaks out the Pi's GPIO, so extra-long headers can be used to attach Pimoroni's [Blinkt](https://shop.pimoroni.com/products/blinkt) or [Mini Black Hat Hacker](https://shop.pimoroni.com/products/mini-black-hat-hack3r).

With a few spare rows on the proto HAT, I added a trio of LEDs so that I could work with relatively simple scripts to get my Python up to speed. The pots and switch can be used to alter values of the outputs like the colour/brightness/blink speed of LEDs, or can just as easily connect with anything else attached to the available GPIO pins.

[Read more](callumkirkwood.com/projects/potHat)

##### Hardware
- Raspberry Pi 2/3/Zero
- Adafruit Perma-Proto Hat
- Extra long female headers
- MCP3008 / other ADC
- 3x 10k potentiometers
- Momentary switch
- 3x LEDs (i.e. red, yellow, green)
- 3x resistors
- Connecting wires

###### Optional
- Sugru (or M2.5 stand-offs if using without a case)
- Pimoroni Blinkt
