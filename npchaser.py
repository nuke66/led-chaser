#import board
#import neopixel
import time

RED = (255,0,0)
#YELLOW = (255,255,0)
#GREEN = (0,255,0)
#BLUE = (0,0,255)
#PURPLE = (153,0,153)
#WHITE = (255,255,255)
#PINK = (255,51,153)

NUMPIXELS = 16


def fill_range(neo,color=RED,start=0,end=NUMPIXELS):
    for n in range(start,end+1):
        neo[n]=color;
    neo.show()    
    

def sweep(neo,color=RED,bgcolor=0,back=False,delay=0.05,start=0,end=NUMPIXELS-1):    
    if(back!=False):
        #sweep up
        print("false range({},{})".format(start,end+1))
        for n in range(start,end+1):
            print("->{}".format(n))
            neo[n]=color
            neo.show()
            time.sleep(delay)
            neo[n]=bgcolor
            neo.show()
    else:
        #sweep down
        print("true range({},{},-1)".format(end-1,start-1))
        for x in range(end-1,start-1,-1):
            print("->{}".format(x))
            neo[x]=color
            neo.show()
            time.sleep(delay)
            neo[x]=bgcolor
            neo.show()

def sweep_fill_range(neo,color=RED,start=0,end=NUMPIXELS,delay=0.05):
    for n in range(start,end+1):
        neo[n]=color
        neo.show()
        time.sleep(delay)

def sweep_range(neo,color=RED,bgcolor=0,start=0,end=NUMPIXELS,delay=0.05):
    for n in range(start,end+1):
        neo[n]=color
        neo.show()
        time.sleep(delay)
        
def sweep_and_stack(neo,color=RED,bgcolor=0,start=0,end=NUMPIXELS-1,delay=0.01):
    neo.fill(bgcolor)
    neo.show()
    for stackPos in range(end,start-1, -1):
        #sweep up
        sweep(neo,color,bgcolor,True,delay,start,stackPos)
        neo[stackPos]=color
        neo.show()
        sweep(neo,color,bgcolor,False,delay,start,stackPos)

def sweep_and_stack_CW(neo,color=RED,bgcolor=0,start=0,end=NUMPIXELS,delay=0.01):
    fill_range(neo,bgcolor,start,end)
    print("range({},{})".format(start,end))
    for stackPos in range(start,end):
        #sweep up
        sweep(neo,color,bgcolor,False,delay,stackPos,end+1)
        neo[stackPos]=color
        print("stackPos:",stackPos)
        neo.show()
        sweep(neo,color,bgcolor,True,delay,stackPos+1,end)
    print("stackPos is {}".format(stackPos))
    neo[stackPos+1]=color
    neo.show()


def one_in_n(neo,color=RED,bgcolor=0,size=2,delay=0.5):
    for n in range(0,size):
        neo.fill(bgcolor)
        neo.show()
        for x in range(n,NUMPIXELS,size):
            neo[x]=color
        neo.show()            
        time.sleep(delay)

def blink_all(neo,color=RED,delay=0.05):
    neo.fill(color)
    neo.show()
    time.sleep(delay)
    neo.fill(0)
    neo.show()
    time.sleep(delay)
    