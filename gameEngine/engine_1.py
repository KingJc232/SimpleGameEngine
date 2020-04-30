"""
Developer: Jc
Goal: To Create a Simple Game Engine /Game FrameWork To help me make simple 2d games using pygame 

Todo: 
		- Colors 				********DONE********

		- State class 			********DONE********

		- Entity Class 			********DONE********

		- Button Class 			********DONE********

	 	- DisplayText 			********DONE********

		- Text box 				

		- Animation 

		- Collision Detection 	AABB Detection

		- Game Class 

		- Create a Simple Website in Royalcraft.co/Jc (That Documents Your Simple Game Engine) (learn a little HTML/ Javascript)


"""

import pygame
import random 
from enum import Enum 
from time import sleep

#Initializing pygame 
pygame.init()


#pygame Colors 
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTGRAY = (200,200,200)
GRAY = (150,150,150)
DARKGRAY = (75,75,75)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,200)
PURPLE = (100,0,100)
LIGHTBLUE = (0,200,255)
PINK = (230,0,230)



#Base Class For All States 
class State:

	def __init__(self):
		self.isActive = False #initially False 

	def update(self,mouseState):
		pass

	def draw(self, screen):
		pass


#Entity Class (all Entities inherit from this class)
class Entity(pygame.Surface):

	def __init__(self,pos, size = (100,100), fillColor = PINK):
		super().__init__(size) #Initializing the size of the entity 
		self.pos = pos #Saving the Position of the entity 
		self.fill(fillColor)
		self.size = size #Saving the Size of the Entity

	#Update Place Holder 
	def update(self,mouseState):
		pass		

	#Draws the Entity to the Screen 
	def draw(self,screen):
		screen.blit(self,self.pos)


#Allows the User to Easily display text on the screen 
class DisplayText:
	def __init__(self, message, pos, textColor = BLACK, sizeOfText = 30, fontFile = "BebasNeue-Regular.ttf"):
		self.font = pygame.font.Font(fontFile,sizeOfText)
		#Saving the textColor
		self.textColor = textColor
		#Creating a text surface object on which text is drawn on to 
		self.text = self.font.render(message, True,textColor)
		#Saving the position of the text
		self.pos = pos 
		#Saving the message 
		self.message = message

	#Changes the Message of the DisplayText Object 
	def update(self, newMessage):
		#Ensures it only changes the message when it has to 
		if self.message != newMessage:
			self.text = self.font.render(newMessage, True, self.textColor)
			self.message = newMessage

	#Draws the DisplayText Object To the Screen 
	def draw(self,screen):
		screen.blit(self.text, self.pos)

#Compacts all the colors of the button into a simple data structure 
class ButtonColor:
	def __init__(self, idleColor = WHITE, hoverColor = GRAY, pressedColor = DARKGRAY):
		self.idleColor = idleColor
		self.hoverColor = hoverColor
		self.pressedColor = pressedColor

#Keeps Track of the Button State 
class ButtonState(Enum):
	IDLE = 1
	HOVER = 2
	PRESSED = 3
#Button Class 
class Button(Entity):

	def __init__(self, message, pos, size = (200,50), buttonColor = ButtonColor()):
		super().__init__(pos,size)

		self.message = message
		self.buttonColor = buttonColor 
		self.buttonState = ButtonState.IDLE #Initially The Button is Idle 

		#message, pos, textColor = BLACK, sizeOfText = 30, fontFile = "BebasNeue-Regular.ttf"
		textPos = (pos[0] + 50, pos[1] )
		self.text = DisplayText(self.message,textPos, BLACK, 50)

		self.isPressed = False #Initially the Button is Not Pressed 

	def update(self, mouseState):

		self.buttonState = ButtonState.IDLE #If Nothing Happening then its IDLE 

		#Getting the Position of the Mouse 
		mousePos = pygame.mouse.get_pos()

		#Checking if the Mouse is Hovering over the Button 
		if mousePos[0] >= self.pos[0] and mousePos[0] <= (self.pos[0] + self.get_width()):
			if mousePos[1] > self.pos[1] and mousePos[1] <= (self.pos[1] + self.get_height()):
				#Mouse is Currently Hovering over the Button 
				self.buttonState = ButtonState.HOVER

				#Check if the button is being pressed 
				if mouseState[0]:
					self.buttonState = ButtonState.PRESSED #Switching the Button State 
					self.isPressed = True # 

	def draw(self, screen, outline = True):

		#Changing the Button Color Based off its State 
		if self.buttonState == ButtonState.IDLE:
			fillColor = self.buttonColor.idleColor
		if self.buttonState == ButtonState.HOVER:
			fillColor = self.buttonColor.hoverColor
		if self.buttonState == ButtonState.PRESSED:
			fillColor = self.buttonColor.pressedColor

		self.fill(fillColor) #Changing the Color Based off the Button State 
		
		#Draws the Button Outline 
		if outline == True:
			pygame.draw.rect(screen, (0,0,0), (self.pos[0] - 2, self.pos[1] -2, self.get_width() + 4, self.get_height() + 4), 0)
			pass
		#Drawing the Button (Using the Entity draw Function)
		super().draw(screen)
		#Drawing the Text Of the button 
		self.text.draw(screen)


def main():

	screen = pygame.display.set_mode((800,800)) #Main Screen 
	screen.fill(RED)

	testEntity = Entity((200,20), (10,300))


	#self, message, pos, textColor = BLACK, sizeOfText = 30, fontFile = "BebasNeue-Regular.ttf"
	text = DisplayText("TEST" , (400,400), LIGHTBLUE, 100)


	#Testing the Button Class 
	#self, message, pos, size = (100,50), buttonColor = ButtonColor()
	testButton = Button("Play", (400,400))


	#Temp Variable Used to Count the DisplayText
	x = 0


	#Game Loop
	isOver = False  
	while(not isOver):

		#Event Loop Handler 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isOver = True #Stop The game loop 

		mouseState = pygame.mouse.get_pressed()

		keys = pygame.key.get_pressed() #Getting a list of booleans of all the keys in the game 

		screen.fill(RED)


		#Testing the Button 
		testButton.update(mouseState)
		testButton.draw(screen)


		pygame.display.update() #Updating the display module 

	pygame.quit() #Quitting pygame 

if __name__ == "__main__":
	main()