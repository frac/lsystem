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

DIR = [(1,0),(0,1),(-1,0),(0,-1)]
PASSO = 1
MARGEM = 25
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
        pos_x = self.pos_x + (DIR[self.dir][0]*PASSO)
        pos_y = self.pos_y + (DIR[self.dir][1]*PASSO)
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
        #print (t[0][0]-self.min_x+MARGEM,t[0][1]-self.min_y+MARGEM),(t[1][0]-self.min_x+MARGEM,t[1][1]-self.min_y+MARGEM)
        return Line((t[0][0]-self.min_x+MARGEM,t[0][1]-self.min_y+MARGEM),(t[1][0]-self.min_x+MARGEM,t[1][1]-self.min_y+MARGEM))
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
    scene = Scene('large_test_%03d.png'%i,height=(caminho.dim_y()+2*MARGEM),width=(caminho.dim_x()+2*MARGEM))
    while(caminho.has_more()):
        scene.add(caminho.linha())
    scene.write_svg()
    #scene.display()


for i in range(20):
    saida = []
    for elem in axiom:
        saida += r1(elem)

    axiom = saida
    #print axiom
    display(axiom, i)

        
