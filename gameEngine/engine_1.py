"""
Developer: Jc
Goal: To Create a Simple Game Engine To help me make simple 2d games using pygame 

Todo: 
		- Colors 

		- Collision Detection 

		- State class

		- Entity Class 

		- Button Class

		- MainMenuState (Simple) 

		- PlayAgainState

		- Animation 

		- Text box 

		- Game Class 

"""

import pygame
import random 

#Initializing pygame 
pygame.init()


#pygame Colors 
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,200)
PURPLE = (102,0,102)
LIGHTBLUE = (0,0,255)


#Entity Class (all Entities inherit from this class)
class Entity(pygame.Surface):

	def __init__(self,pos, fillColor = LIGHTBLUE, size = (100,100)):
		super().__init__(size) #Initializing the size of the entity 
		self.pos = pos #Saving the Position of the entity 
		self.fill(fillColor)


	#Update Place Holder 
	def update(self,mouseState):
		pass		

	#Draws the Entity to the Screen 
	def draw(self,screen):
		screen.blit(self,self.pos)

#Button Class 



def main():

	screen = pygame.display.set_mode((800,800)) #Main Screen 

	screen.fill(BLACK)

	#Game Loop
	isOver = False  
	while(not isOver):

		#Event Loop Handler 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isOver = True #Stop The game loop 


		pygame.display.update() #Updating the display module 

	pygame.quit() #Quitting pygame 

if __name__ == "__main__":
	main()