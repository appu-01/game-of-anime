from pygame import*

screen = display.set_mode((1000,700))

running=True
first=True
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    if first:
        for x in range(0,1000):
            for y in range(0,700):
                screen.set_at((x,y),(111,255,111))
                display.flip()
        first=False

    display.flip()
quit()
