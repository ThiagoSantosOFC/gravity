# src/game/__init__.py

import pygame
from src.player import Player
from src.map import Map
from src.physics import Physics
from src.powerups import Powerups
from src.multiplayer import Multiplayer

class Game:
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.map = Map()
        self.physics = Physics(self.players, self.map)
        self.powerups = Powerups(self.players)
        self.multiplayer = Multiplayer(self.players)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                for player in self.players:
                    player.handle_input(event)

    def update(self):
        self.physics.update()
        self.powerups.update()
        self.multiplayer.update()

        if self.check_winner():
            self.running = False

    def render(self):
        self.map.render()
        for player in self.players:
            player.render()

    def check_winner(self):
        for player in self.players:
            if player.has_won():
                return True
        return False
