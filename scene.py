# Tamsin Rogers
# November 12, 2019
# CS 152 
# Project 10: Rotating Pinball
# run this program from the Terminal by entering "python3 scene.py"
# this program creates a pinball simulation using ball, block, triangle, and rotating block objects, and user interaction

#import the physics_objects file, collision file, and graphicsPlus package
import physics_objects as pho
import collision
import graphicsPlus as gr
import random
import time
import math
from graphicsPlus import *

"""This function creates all of the obstacles in the scene and puts them into a list called theshapes."""
def buildObstacles(win):
	#the walls
	rightwall = pho.Block(win)
	rightwall = pho.Block(win)
	rightwall.setPosition(50,0)
	rightwall.setHeight(100)
	rightwall.setWidth(1.5)
	rightwall.setColor((0,0,0))
	leftwall = pho.Block(win)
	leftwall.setPosition(0,50)
	leftwall.setHeight(100)
	leftwall.setWidth(1.5)
	leftwall.setColor((0,0,0))
	topwall = pho.Block(win)
	topwall.setPosition(0,50)
	bottomwall = pho.Block(win)
	bottomwall.setPosition(10,0)
	#the blocks
	block1 = pho.RotatingBlock(win, x0=10, y0=10, Ax=10, Ay=10, width=2, height=2)
	block1.setElasticity(.3)
	block1.setRotVelocity(108)
	block2 = pho.RotatingBlock(win, x0=19.5, y0=19.5, Ax=19.5, Ay=19.5, width=2, height=2)
	block2.setElasticity(.3)
	block2.setRotVelocity(108)
	block3 = pho.RotatingBlock(win, x0=30, y0=30, Ax=30, Ay=30, width=2, height=2)
	block3.setElasticity(.3)
	block3.setRotVelocity(108)
	block4 = pho.RotatingBlock(win, x0=38, y0=38, Ax=38, Ay=38, width=2, height=2)
	block4.setElasticity(.3)
	block4.setRotVelocity(108)
	#the triangles
	triangle1 = pho.Triangle(win)
	triangle1.setPosition(15,15)
	triangle1.setColor((124,54,255))
	triangle2 = pho.Triangle(win)
	triangle2.setPosition(30,40)
	triangle2.setColor((152,97,255))
	triangle3 = pho.Triangle(win)
	triangle3.setPosition(30,10)
	triangle3.setColor((192,158,255))
	triangle4 = pho.Triangle(win)
	triangle4.setPosition(7,40)
	triangle4.setColor((224,207,255))	
	#the balls
	ball1 = pho.Ball(win)
	ball1.setPosition(15,30)
	ball1.setRadius(3)
	ball1.setColor((255,207,207))
	ball1.setElasticity(3)
	ball2 = pho.Ball(win)
	ball2.setPosition(30,15)
	ball2.setRadius(1.5)
	ball2.setColor((255,130,130))
	ball2.setElasticity(1)
	# Return the list of Things
	thewall = [topwall, bottomwall, leftwall, rightwall, block1, block2, block3, block4, triangle1, triangle2, triangle3, triangle4, ball1, ball2]
	return thewall

"""The main function creates a new graphics window, calls the previously defined buildObstacles 
function, and stores the return list in the shapes variable.  It then loops over the shapes 
list to draw the objects in the window and sets up timing and frames.  This function also 
contains logistics for determining if a ball has moved outside of the window or collided 
with another object. """
def main():
	win = gr.GraphWin( 'pinball', 500, 500, False )		#create a GraphWin
	win.setBackground("lightyellow")							#set the color of the background of the window to light yellow
	textbox = gr.Text( gr.Point( 250, 50 ), ("Use the arrow keys to reposition \n the block and bounce the ball") )
	textbox.setSize(15)
	textbox.setTextColor("blue")
	textbox.setStyle('bold')
	textbox.draw(win)
	textbox2 = gr.Text( gr.Point( 250, 90 ), ("Press space to set the color of the ball") )
	textbox2.setSize(15)
	textbox2.setTextColor("red")
	textbox2.setStyle('bold')
	textbox2.draw(win)
	
	shapes = buildObstacles(win)						#callbuildObstacles, storing the return list in a variable
	for i in shapes:									#loop over the shapes list and have each Thing call its draw method
		i.draw()
	dt = 0.02
	frame = 0

	
	ball = pho.Ball(win)		#create the main ball
	ball.setPosition( 20, 30 )
	ball.setVelocity( 20, 20 )
	ball.setAcceleration( 0, -20 )
	ball.setElasticity(2)
	ball.setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
	ball.draw()
		
	catcher = pho.Block(win)	#create the user-controlled block for the ball to bounce off
	catcher.setHeight(1.5)
	catcher.setWidth(10)
	catcher.setPosition(5,1.5)
	catcher.setColor((0,0,250))
	catcher.setElasticity(1)
	catcher.draw()
	
	coloring = True   			#set the coloring flag to True
	
	# start an infinite loop
	while True:
		key = win.checkKey()
		if frame%10 == 0:
			win.update()

		#USER KEY CONTROLS
		if key == "q":			#if the user typed a 'q' then break
			break
		if key == 'Left':		#if the user clicked the left arrow button, move the catcher block to the left
			catcher.moveLeft()
		if key == 'Right':		#if the user clicked the right arrow button, move the catcher block to the right
			catcher.moveRight()				   
		if key == 'Up':			#if the user clicked the up arrow button, move the catcher block up
			catcher.moveUp()
		if key == 'Down':		#if the user clicked the down arrow button, move the catcher block down
			catcher.moveDown()			
		if key == 'space':		#if the user clicked the space key
			coloring = False	#set the coloring flag to False
		if coloring:
			ball.setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))	#set the ball to a random color
		
		# if the ball is out of bounds, re-launch it
		if ball.getPosition()[0] > win.getWidth() or ball.getPosition()[1] < 0: #if the ball is outside the window
			ball.setPosition(25, 25)											#reposition the ball to the center of the window
			ball.setVelocity(random.randint(0,10), random.randint(0,10))		#give the ball a random velocity
			ball.update(.01)
		
		collided = False
		for i in shapes:
			if collision.collision(ball, i, .01) == True:
				collided = True
		if collision.collision(ball, catcher, .01) == True:
			collided = True
		if collided == False:
			ball.update(dt)
		frame = frame + 1

		shapes[4].update(dt)
		shapes[5].update(dt)
		shapes[6].update(dt)
		shapes[7].update(dt)
	
	win.getMouse()
	win.close()		  

if __name__ == "__main__":
	main()