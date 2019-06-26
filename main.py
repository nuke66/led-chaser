# Run a demo of the npchaser and npchasery led chaser functions.
import board
import neopixel
import time

from npchaser import *
from npchasery import *

NUMPIXELS = 16
neo = neopixel.NeoPixel(board.D5, NUMPIXELS, brightness=0.02, auto_write=False)

#colours
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (153,0,153)
WHITE = (255,255,255)
PINK = (255,51,153)

def run():
    print("\nNeopixel Led Chaser")
    neo.fill(0)
    neo.show()
    
def npchaser_test(): 
    print("\nChaser test ***\n") 
    
    sweep(neo,BLUE,RED,False,0.05,0,7)
    
    for n in range(1,5):
        one_in_n(neo,PINK,0,2,0.3)
    for n in range(1,5):
        one_in_n(neo,RED,YELLOW,2,0.3)
    for n in range(1,5):
        one_in_n(neo,PINK,0,4,0.3)
    for n in range(1,5):
        one_in_n(neo,RED,BLUE,4,0.3)    
    time.sleep(2)
 
    sweep_and_stack(neo,YELLOW)
    sweep_and_stack(neo,GREEN,RED)
    neo.fill(0)
    neo.show()
 
    sweep_fill_range(neo,RED,0,3)
    sweep_fill_range(neo,YELLOW,4,7)
    sweep_fill_range(neo,GREEN,8,11)
    sweep_fill_range(neo,BLUE,12,15)

    sweep_fill_range(neo,PURPLE,0,3)
    sweep_fill_range(neo,WHITE,4,7)
    sweep_fill_range(neo,PINK,8,11)
    sweep_fill_range(neo,RED,12,15)

    sweep_fill_range(neo,YELLOW,0,3)
    sweep_fill_range(neo,GREEN,4,7)
    sweep_fill_range(neo,BLUE,8,11)
    sweep_fill_range(neo,PURPLE,12,15)

    sweep_fill_range(neo,WHITE,0,3)
    sweep_fill_range(neo,PINK,4,7)
    sweep_fill_range(neo,RED,8,11)
    sweep_fill_range(neo,YELLOW,12,15)
    time.sleep(2)
    neo.fill(0)
    neo.show()
    
    fill_range(neo,BLUE,0,3)
    time.sleep(0.5)
    fill_range(neo,GREEN,4,7)
    time.sleep(0.5)
    fill_range(neo,RED,8,11)
    time.sleep(0.5)
    fill_range(neo,YELLOW,12,15)
    time.sleep(0.5)
    
    for n in range(1,7):          
        # pos 1
        fill_range(neo,YELLOW,0,3)
        fill_range(neo,BLUE,4,7)
        fill_range(neo,GREEN,8,11)
        fill_range(neo,RED,12,15)
        time.sleep(0.3)
    
        # pos 2
        fill_range(neo,RED,0,3)
        fill_range(neo,YELLOW,4,7)
        fill_range(neo,BLUE,8,11)
        fill_range(neo,GREEN,12,15)
        time.sleep(0.3)
    
        # pos 3
        fill_range(neo,GREEN,0,3)
        fill_range(neo,RED,4,7)
        fill_range(neo,YELLOW,8,11)
        fill_range(neo,BLUE,12,15)
        time.sleep(0.3)
    
        # pos 4
        fill_range(neo,BLUE,0,3)
        fill_range(neo,GREEN,4,7)
        fill_range(neo,RED,8,11)
        fill_range(neo,YELLOW,12,15)
        time.sleep(0.3)
        
    neo.fill(0)
    one_in_n(neo)
    one_in_n(neo,PINK)
    one_in_n(neo,YELLOW,4)
    
    blink_all(neo,BLUE,0.5)
    blink_all(neo,GREEN,0.5)
    blink_all(neo,PINK,0.5)
    sweep(neo)
    sweep(neo,GREEN)
    sweep(neo,BLUE)
    sweep(neo,PINK)
    sweep(neo,PINK,0,True)
    sweep(neo,WHITE,YELLOW)
    sweep(neo,WHITE,YELLOW,True)
    sweep(neo,BLUE,YELLOW)
    sweep(neo,PINK,YELLOW,True)
    sweep(neo,GREEN,YELLOW)
    sweep(neo,RED,YELLOW,True)
    neo.fill(0)
    neo.show()


def npchasery_test():
    print("\nChaser YIELD test ***\n")
    for x, y in zip(y_sweep_stack_CW(neo, 0, 7, RED),y_sweep_stack(neo, 8, 15, RED)):
        neo.show()
        time.sleep(0.01)

    for x, y in zip(y_sweep_stack(neo, 0, 7, RED),y_sweep_stack(neo, 8, 15, BLUE)):
        neo.show()
        time.sleep(0.01)

    for a1, b2 in zip(y_fill(neo,0,7,RED),y_fill(neo,8,15,BLUE)):
        time.sleep(0.2)
        neo.show()
    time.sleep(0.5)
    
    for a1, b2 in zip(y_fill(neo, 0,7,BLUE,WHITE),y_fill(neo, 8,15,YELLOW,GREEN)):
        time.sleep(0.2)
        neo.show()
    time.sleep(0.5)

    for a1, b2, c3, d4 in zip(y_fill(neo, 0,3,RED),y_fill(neo, 4,7,BLUE),y_fill(neo, 8,11,YELLOW),y_fill(neo, 12,15,GREEN)):
        time.sleep(0.1)
        neo.show()
    time.sleep(0.3)
    for a1, b2, c3, d4 in zip(y_fill(neo, 0,3,GREEN),y_fill(neo, 4,7,RED),y_fill(neo, 8,11,BLUE),y_fill(neo, 12,15,YELLOW)):
        time.sleep(0.15)
        neo.show()
    time.sleep(0.3)    
    for a1, b2, c3, d4 in zip(y_fill(neo, 0,3,YELLOW),y_fill(neo, 4,7,GREEN),y_fill(neo, 8,11,RED),y_fill(neo, 12,15,BLUE)):
        time.sleep(0.15)
        neo.show()
    time.sleep(0.3)
    for a1, b2, c3, d4 in zip(y_fill(neo, 0,3,BLUE),y_fill(neo, 4,7,YELLOW),y_fill(neo, 8,11,GREEN),y_fill(neo, 12,15,RED)):
        time.sleep(0.15)
        neo.show()
    time.sleep(0.3)
    for a1, b2, c3, d4 in zip(y_fill(neo, 0,3,RED),y_fill(neo, 4,7,BLUE),y_fill(neo, 8,11,YELLOW),y_fill(neo, 12,15,GREEN)):
        time.sleep(0.1)
        neo.show()
    time.sleep(0.3)

def run():
    while True:
        npchasery_test()
        npchaser_test()

run()