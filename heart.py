from karel.stanfordkarel import *

def main():
    center()
    rightside()
    rightside()
    middle()
    turn_right()
    rightside()
    turn_left()
    move()
    leftside()
    for i in range(2):
        move()
    

def center():
    turn_left()
    for i in range(3):
        move()
    turn_right()
    for i  in range(4):
        move()
    put_beeper()
    move()
    put_beeper()
    
def rightside():
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()

def ahead():
    turn_left()
    move()
    put_beeper()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def middle():
    ahead()
    ahead()
    turn_left()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()

def leftside():
    ahead()
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()
    move()
    turn_left()
    move()
    
# don't change this code
if __name__ == '__main__':
    main()
