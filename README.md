# led-chaser
CircuitPython led chaser for NeoPixels (RGB) 

This was a fun project to do. Working with a circle of leds made me think up more interesting patterns than I had previously with just a straight 'bar' of lights.  I also got to use generators to help solve one of the more complex sequences (npchasery.py).

I developed this on an AdaFruit 16 x WS2812 5050 NeoPixel Ring using a Adafruit ItsyBitsy M0 Express.  Generally I haven't have any issues except when trying to run more complex sequences on bright settings - I feel like I'm hitting timing and power issues at the same time.

If I get time I'll clean up the code, put it into classes, and make a .mpy library for it.
