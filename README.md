# led-chaser
Circuit python led chaser for neo pixels. 

I had fun putting this together.  Although you can use straight LED strips I find the circular ones look really good and made me think more about the different sequences I could do

My sequences stay within the array index, i.e. they don't wrap around.




Originally tested on an AdaFruit 16 x WS2812 5050 NeoPixel Ring using a Adafruit ItsyBitsy M0 Express.  Supposedly you can run into timing issues using timing issues when using Python (uPython, circuitpython, etc) instead of an AVR (arduino, etc).  Generally I haven't had problems, when I have it has been at complex sequences on bright settings (power/timing issues combined?)
