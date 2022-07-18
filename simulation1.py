import numpy as np 
import matplotlib 
import turtle 
import time 

#global parameters##
TIMER = 0 
TIME_STEP = 0.5
SETPOINT = 10
SIM_TIME = 10
INITIAL_X = 0
INITIAL_Y = -100
MASS = 1 #kg
MAX_THRUST = 15 #newtons 
g = -9.81 #constant gravitational 
V_i = 0 #initial velocity 
Y_i = 0 #initial height 


##############


class Simulation(object):
    def __init__(self):
        self.Insight = Rocket()
        self.screen = turtle.Screen()
        self.screen.setup(1280, 900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15, SETPOINT) 
        self.marker.color('red')
        self.sim = True 
        self.timer = 0
    def cycle(self):
        while(self.sim):
        #get a thrust output from our PID 
            thrust = 8 #newtonws 
            self.Insight.set_ddy(thrust)
            self.Insight.set_dy()
            self.Insight.set_y()
            time.sleep(TIME_STEP)
            self.timer += 1
            if self.timer > SIM_TIME:
                self.sim = False 
            elif self.Insight.get_y() > 800:
                self.sim = False 
            elif self.Insight.get_y() < -400:
                self.sim = False 

class Rocket(object):
    def __init__(self):
        global Rocket
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('square')
        self.Rocket.color('black')
        self.Rocket.penup()
        self.Rocket.goto(INITIAL_X, INITIAL_Y)
        self.Rocket.speed(0)
        #physics 
        self.ddy = 0
        self.dy = V_i
        self.y = INITIAL_Y
    def set_ddy(self, thrust):
        self.ddy = g + thrust / MASS
    def get_ddy(self):
        return self.ddy
    def set_dy(self):
        self.dy += self.ddy
    def get_dy(self):
        return self.dy
    def set_y(self):
        self.Rocket.sety(self.y + self.dy)
    def get_y(self):
        self.y = rocket.ycor()
        return self.y 




def main():
        while(TIMER < 10):
            sim = Simulation()
            time.sleep(1)
            timer += 1

main() 