# Author: Marko "Geohot" Petrov
# OpenMind Chess Artificial Intelligence
# Version 0.0.1 
import pygame
from chess_engine import *
from chess_rules import *

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
			self.pieceIMAGES[piece] = pygame.transform.scale(pygame.image.load(r"C:/Users/User/OpenMInd/geohot_chess/" + piece + ".png"), (GSettings.SQSize, GSettings.SQSize))
			# Load all piece images in Dictionary

	def update(self, screen):
		return 0;
	def main():
		pygame.init()
		screen = pygame.display.set_mode((GSettings.Width, GSettings.Height))
		screen.fill(pygame.Color("white"))
		clock = pygame.time.Clock()
		Gstats = Game_Stats()
		running = True
		while running:


