# Author: Marko "Geohot" Petrov
# OpenMind Chess Artificial Intelligence
# Version 0.0.1

import pygame
from chess_engine import *
from chess_rules import *
import numpy as np
#import TensorFlow as tf
import math as m

class Game:
	def __init__(self):
		self.Height = 500
		self.Width = 500
		self.Dimensions = 8 # Number of squares per row and column
		self.SQSize = self.Width//self.Dimensions
		self.MaxFPS = 15 # Will Update later For animations
		self.pieceIMAGES = {}


	def load_images(self):
		pieces = ['wR','wQ','wp','wN','wK','wB','bR','bQ','bp','bN','bK','bB']
		for piece in pieces:
			self.pieceIMAGES[piece] = pygame.transform.scale(pygame.image.load(r"C:/Users/User/OpenMInd/geohot_chess/" + piece + ".png"), (self.SQSize, self.SQSize))
			# Load all piece images in Dictionary

	# Draw all the colors and pieces on the board
	def draw_board(self, screen):
		Colors = [pygame.Color("white"), pygame.Color("gray")]
		for r in range(8):
			for c in range(8):
				color = Colors[((r+c) % 2)]
				pygame.draw.rect(screen, color, pygame.Rect(c*self.SQSize, r*self.SQSize, self.SQSize, self.SQSize))


	def draw_pieces(self, screen, board):
		for r in range(self.Dimensions):
			for c in range(self.Dimensions):
				piece = board[r][c]
				if piece != '--': # Is not Empty
					screen.blit(self.pieceIMAGES[piece], pygame.Rect(c*self.SQSize, r*self.SQSize, self.SQSize, self.SQSize))


	def update(self, screen, board):
		self.draw_board(screen)
		self.draw_pieces(screen, board)
		pygame.display.flip()


	def main(self):
		pygame.init()
		screen = pygame.display.set_mode((self.Width, self.Height))
		screen.fill(pygame.Color("white"))
		clock = pygame.time.Clock()
		Gstats = GameState()
		running = True
		self.load_images()
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False 
			self.update(screen, Gstats.board)


StartGame = Game()
if __name__ == "__main__":
	StartGame.main()

