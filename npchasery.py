#npchasery.py
# Neopixel chaser with yield (generators)

NUMPIXELS = 16

def y_fill(neo, start, end, color=(255,0,0), bgcolor=0):
  #blank out range
  for n in range(start,end+1):
    neo[n]=bgcolor
  yield 'start'
  #fill up range
  for x in range(start,end+1):
    neo[x]=color
    yield x
 
  #fill down range
  for y in range(end,start-1,-1):
    neo[y]=bgcolor
    yield y

def y_sweep_stack(neo, start=0, end=NUMPIXELS, color=(255,0,0), bgcolor=0):
    for stackPos in range(end,start,-1):
        for n in range(start,stackPos+1):
            neo[n]=color;
            yield n
            neo[n]=bgcolor
            yield n
        neo[stackPos]=color        

        for x in range(stackPos-1,start-1,-1):
            neo[x]=color
            yield x
            neo[x]=bgcolor
            yield x
        neo[start]=color
        yield x

def y_sweep_stack_CW(neo, start=0, end=NUMPIXELS, color=(255,0,0), bgcolor=0):
    for stackPos in range(start,end):
        for x in range(end,stackPos-1,-1):
            neo[x]=color
            yield x
            neo[x]=bgcolor
            yield x        

        neo[x]=color        
        
        for n in range(stackPos+1,end+1):
            neo[n]=color
            yield n
            neo[n]=bgcolor
            yield n

        neo[end]=color
        yield n