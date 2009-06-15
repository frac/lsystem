import os
import Image, ImageDraw

display_prog = 'display' # Command to execute to display images.


class Scene:
    def __init__(self,name="png",height=400,width=400):
        self.name = name
        self.items = []
        self.height = height
        self.width = width
        self.im = Image.new("RGB", (self.width, self.height), "white")
        self.draw = ImageDraw.Draw(self.im)


        return

    def add(self,item): 
        self.items.append(item)

    def strarray(self):
        var = ["<?xml version=\"1.0\"?>\n",
               "<svg height=\"%d\" width=\"%d\" >\n" % (self.height,self.width),
               " <g style=\"fill-opacity:1.0; stroke:black;\n",
               "  stroke-width:1; stroke-linecap:round;\">\n"]
        for item in self.items: var += item.strarray()            
        var += [" </g>\n</svg>\n"]
        return var

    def write_svg(self,filename=None):
        for line in self.items:
            line.imprimir(self.draw)

        self.im.save(self.name, "PNG")

        return

    def display(self,prog=display_prog):
        os.system("%s %s" % (prog,self.svgname))
        return        
        

class Line:
    def __init__(self,start,end):
        self.start = start #xy tuple
        self.end = end     #xy tuple
        return

    def imprimir(self, draw):
        draw.line((self.start[0],self.start[1],self.end[0],self.end[1]), 128)
        
    def strarray(self):
        return ["  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" />\n" %\
                (self.start[0],self.start[1],self.end[0],self.end[1])]



