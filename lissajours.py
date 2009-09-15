#!/usr/bin/python
# coding:utf8

from pilscene import *
from math import sin, cos, pi, trunc
import random

class Lissajour(object):
    def __init__(self,max_x, max_y):
        self.delta = 0.001
        self.max_x = max_x
        self.max_y = max_y
        self.pos = (0,max_y/2)
        self.a = self.max_x 
        self.b = self.max_y 
        self.alfa = pi
        self.beta = pi
        self.ang = [0,0]

        self.tracos = []
        
    def run(self,times):
        for i in range(times):
            t = i * self.delta
            self.calcpos(t)
    def recalc(self,t):
        mod = trunc(t*self.delta)
        print t,mod
        self.alfa += mod * 0.1 * (0.5 - random.random())
        self.beta += mod * 0.1 * (0.5 - random.random())
        #print self.alfa, self.beta



    def calcpos(self,t):
        self.recalc(t)
        self.ang[0] += self.alfa * self.delta
        self.ang[1] += self.beta * self.delta
        x = self.pos[0] + self.delta * self.a * sin(self.ang[0])
        y = self.pos[1] + self.delta * self.b * cos(self.ang[1])
        #y = self.b * cos(self.beta * t)
        #print x,y, self.pos
        self.tracos.append( ((self.pos[0], self.pos[1]),(x,y)) )
        self.pos=(x,y)

    def linha(self):
        t = self.tracos.pop(0)
        #print t
        return Line((t[0][0]+MARGEM,t[0][1]+MARGEM),(t[1][0]+MARGEM,t[1][1]+MARGEM))
    def has_more(self):
        return len(self.tracos) >= 1
    def dim_x(self):
        return self.max_x 
    def dim_y(self):
        return self.max_y 
        


        

MARGEM = 25
def display(caminho):
    #caminho.imprime()
    scene = Scene('large_lissajour_rand_%03d.png'%len(caminho.tracos),height=(caminho.dim_y()+2*MARGEM),width=(caminho.dim_x()+2*MARGEM))
    while(caminho.has_more()):
        scene.add(caminho.linha())
    scene.write_svg()
    #scene.display()

def gera_video(caminho):
    #caminho.imprime()
    i = 1
    count = 1
    scene = Scene('foo',height=(caminho.dim_y()+2*MARGEM),width=(caminho.dim_x()+2*MARGEM))
    while(caminho.has_more()):
        scene.add(caminho.linha())
        if count % i == 0:
            scene.write_svg("video_frame%05d.jpg"% i)
            i += 1
            count = 1
        else:
            count += 1
    scene.display()


if __name__ == "__main__":
    caminho = Lissajour(500,500)
    caminho.run(100000)
    display(caminho)

#gera_video(axiom)            
