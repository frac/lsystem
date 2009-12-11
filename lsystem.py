#!/usr/bin/python
# coding:utf8

from pilscene import *
"""
    variables : X Y
    constants : F + −
    start  : FX
    rules  : (X → X+YF), (Y → FX-Y)
    angle  : 90°

omega = ((X,Y),(F,+,-),FX,((X → X+YF), (Y → FX-Y)))
"""

axiom = ["F","X"]

def r1(elemento):
    if elemento == "X":
        return ["X","+","Y","F"]
    elif elemento == "Y":
        return ["F","X","-","Y"]
    else:
        return elemento

##
##Constants
##

DIR = [(1,0),(0,1),(-1,0),(0,-1)]
STEP = 5
MARGIN = 25
NUM_INTERACTIONS = 15 #beware of larger values for this

class Caminho(object):
    def __init__(self):
        self.dir = 0
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.tracos = []
        self.pos_x = 0
        self.pos_y = 0
    def traco(self):
        pos_x = self.pos_x + (DIR[self.dir][0]*STEP)
        pos_y = self.pos_y + (DIR[self.dir][1]*STEP)
        self.tracos.append( ((self.pos_x, self.pos_y),(pos_x,pos_y)) )
        self.pos_x = pos_x
        self.pos_y = pos_y
        if self.pos_x > self.max_x:
            self.max_x = self.pos_x
        if self.pos_y > self.max_y:
            self.max_y = self.pos_y
        if self.pos_x < self.min_x:
            self.min_x = self.pos_x
        if self.pos_y < self.min_y:
            self.min_y = self.pos_y

    def esquerda(self):
        self.dir = (self.dir + 1) % 4
    def direita(self):
        self.dir -= 1
        if self.dir < 0:
            self.dir = 3
    def imprime(self):
        print ((self.min_x, self.min_y), (self.max_x, self.max_y))
        print self.tracos
    def dim_x(self):
        return self.max_x - self.min_x
    def dim_y(self):
        return self.max_y - self.min_y
    def linha(self):
        t = self.tracos.pop(0)
        #print "adding line ", t
        #print (t[0][0]-self.min_x+MARGIN,t[0][1]-self.min_y+MARGIN),(t[1][0]-self.min_x+MARGIN,t[1][1]-self.min_y+MARGIN)
        return Line((t[0][0]-self.min_x+MARGIN,t[0][1]-self.min_y+MARGIN),(t[1][0]-self.min_x+MARGIN,t[1][1]-self.min_y+MARGIN))
    def has_more(self):
        return len(self.tracos) >= 1
        


def display(axiom, i):
    caminho = Caminho()
    for elem in axiom:
        if elem == "F":
            caminho.traco()
        if elem == "+":
            caminho.direita() 
        if elem == "-":
            caminho.esquerda() 
    #caminho.imprime()
    scene = Scene('large_test_%03d.png'%i,height=(caminho.dim_y()+2*MARGIN),width=(caminho.dim_x()+2*MARGIN))
    while(caminho.has_more()):
        scene.add(caminho.linha())
    scene.write_svg()
    #scene.display()

def gera_video(axiom):
    caminho = Caminho()
    for elem in axiom:
        if elem == "F":
            caminho.traco()
        if elem == "+":
            caminho.direita() 
        if elem == "-":
            caminho.esquerda() 
    #caminho.imprime()
    i = 1
    count = 1
    scene = Scene('foo',height=(caminho.dim_y()+2*MARGIN),width=(caminho.dim_x()+2*MARGIN))
    while(caminho.has_more()):
        scene.add(caminho.linha())
        if count % i == 0:
            scene.write_svg("video_frame%05d.jpg"% i)
            i += 1
            count = 1
        else:
            count += 1
    #scene.display()



for i in range(NUM_INTERACTIONS):
    saida = []
    for elem in axiom:
        saida += r1(elem)

    axiom = saida
    #print axiom
    display(axiom, i)

gera_video(axiom)            
