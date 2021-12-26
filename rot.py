# Tamsin Rogers
# November 13, 2019
# CS 152 
# Lab 10: Geometric Thinking

import graphicsPlus as gr
import math
import time

class RotatingLine:
	def __init__(self, win, x0, y0, length, Ax = None, Ay = None):
		self.pos = [x0,y0]						#The x0 and y0 values as a 2-element list.
		self.length	= length			#The length of the line.
		self.anchor	= [Ax, Ay]			#the Ax and Ay values as a 2-element list, if both are given, otherwise x0, y0 (this involves an if statement)
		if Ax != None and Ay != None:
			self.anchor = [Ax, Ay]
		else:
			self.anchor = [x0,y0]
		self.points	= [(-length/2.0, 0.0), (length/2.0, 0.0)]	#A list that holds two 2-element lists (details below).
		self.angle = 0.0				#The current orientation of the line. Initialize it to 0.0.
		self.rvel = 0.0					#Rotational velocity (in degrees/s). Initialize it to 0.0.
		self.win = win					#A GraphWin object reference.
		self.scale	= 10				#The scale factor from model coordinates to screen coordinates.
		self.vis = []					#A list to hold the graphics Line object. Set it to the empty list, for now.
		self.drawn	= False				#A Boolean variable to indicate if the Line has been drawn. Set it to False.
	
	def render(self):
		# assign to theta the result of converting self.angle from degrees to radians
		theta = self.angle*((math.pi)/180)
		# assign to cth the cosine of theta
		cth = math.cos(theta)
		# assign to sth the sine of theta
		sth = math.sin(theta)
		# assign to pts the empty list
		pts = []
		# for each vertex in self.points
		for v in self.points:
		  # (2 lines of code): assign to x and y the result of adding the vertex to self.pos and subtracting self.anchor
		  x = self.pos[0] + v[0] - self.anchor[0]
		  y = self.pos[1] + v[1] - self.anchor[1]
		  # assign to xt the calculation x * cos(Theta) - y * sin(Theta) using your precomputed cos/sin values above
		  xt = (x*cth - y*sth)
		  # assign to yt the calculation x * sin(Theta) + y * cos(Theta)
		  yt = (x*sth + y*cth)
		  # (2 lines of code): assign to x and y the result of adding xt and yt to self.anchor
		  x = (xt+yt)+self.anchor[0]
		  y = (xt+yt)+self.anchor[1]
		  # append to pts a Point object with coordinates (self.scale * x, self.win.getHeight() - self.scale*y)
		  pts.append(gr.Point(self.scale*x, self.win.getHeight() - self.scale*y))
		# assign to self.vis a list with a Zelle graphics Line object using the Point objects in pts
		self.vis = [gr.Line(pts[0], pts[1])]
		
	def refresh(self):
		drawn = self.drawn
		if drawn:
			self.vis[0].undraw()
			self.render()
			if drawn:
				self.vis[0].draw(self.win)
				
	def getAngle(self):
		return self.angle
	
	def setAngle(self, a):
		self.angle = a
		self.refresh()
	
	def rotate(self, r):
		self.angle = self.angle + r
		if self.drawn:
			self.vis[0].undraw()
			self.vis[0].draw(self.win)

def test1():
    win = gr.GraphWin('line thingy', 500, 500, False)

    line = RotatingLine(win, 25, 25, 10)
    line.render()
    line.vis[0].draw(win)
    line.drawn = True

    while win.checkMouse() == None:
        line.rotate(3)
        time.sleep(0.08)
        win.update()

    win.getMouse()
    win.close()

if __name__ == "__main__":
    test1()