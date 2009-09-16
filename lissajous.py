#!/usr/bin/python
# coding:utf8

from pilscene import *
from math import sin, cos, pi, floor
import random
POS = 0
ANG = 1
VEL = 2
LINES = 3

SPAWN = 0.00001


class Lissajour(object):
    def __init__(self,max_x, max_y):
        self.delta = 0.01
        self.max_x = max_x
        self.max_y = max_y
#        self.pos = (0,max_y/2)
        self.a = self.max_x * pi / 2
        self.b = self.max_y * pi / 2
        self.alfa = 3*pi
        self.beta = 1*pi + self.alfa
#        self.ang = [0,0]
        self.delta_ang = 0.00001
        self.tracos = []
        self.cria_traco(x=0,y=max_y/2,ang_x=0,ang_y=0,alfa=self.alfa,beta=self.beta)

    def cria_traco(self, x=0,y=0,ang_x=0,ang_y=0,alfa=0,beta=0):
        traco = [[x,y],[ang_x,ang_y],[alfa,beta],[]]
        self.tracos.append(traco)
        return traco
        
    def run(self,times):
        for i in range(times):
            if i % 100 == 0:
                print i, len(self.tracos)
            t = i * self.delta
            self.calcpos(t)
    def recalc(self,traco,t):
        traco[VEL][0] *= 5 * (0.5 - random.random()) 
        traco[VEL][1] *= 5 * (0.5 - random.random())
        #print self.alfa, self.beta



    def calcpos(self,t):
        for traco in self.tracos:
            if abs(traco[POS][0]) > self.max_x + MARGEM or abs(traco[POS][1]) > self.max_y + MARGEM :
                continue
            if random.random() <= SPAWN * t and len(self.tracos) < 5:
                tmptraco = self.cria_traco(x=traco[POS][0],y=traco[POS][1],ang_x=traco[ANG][0],ang_y=traco[ANG][1],alfa=traco[VEL][0],beta=traco[VEL][1])
                self.recalc(tmptraco,t)
            delta_x = traco[VEL][0] * self.delta + self.delta_ang
            delta_y = traco[VEL][1] * self.delta
            traco[ANG][0] += delta_x
            traco[ANG][1] += delta_y
            x = traco[POS][0] + delta_x * self.a * sin(traco[ANG][0]) / pi
            y = traco[POS][1] + delta_y * self.b * cos(traco[ANG][1]) / pi
            #y = self.b * cos(self.beta * t)
            #print x,y, self.pos
            traco[LINES].append( ((traco[POS][0], traco[POS][1]),(x,y)) )
            traco[POS]=[x,y]

    def linha(self):
        for traco in self.tracos:
            t = traco[LINES].pop(0)
            if len(traco[LINES]) == 0:
                self.tracos.pop(0)
            return Line((t[0][0]+MARGEM,t[0][1]+MARGEM),(t[1][0]+MARGEM,t[1][1]+MARGEM))


    def has_more(self):
        return len(self.tracos) >= 1
    def dim_x(self):
        return self.max_x 
    def dim_y(self):
        return self.max_y 
        


        

MARGEM = 25
import os
def display(caminho):
    #caminho.imprime()
    i = 1
    while i:
        nome = '%04d.png'%i
        i += 1
        if not os.path.isfile(nome):
            break

    print nome
    scene = Scene(nome,height=(caminho.dim_y()+2*MARGEM),width=(caminho.dim_x()+2*MARGEM))
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
    caminho.run(int(pi * 2000))
    display(caminho)

#gera_video(axiom)            
