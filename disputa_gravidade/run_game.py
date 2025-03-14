import pygame
from src.game import Game

def main():
    # Inicializar o Pygame
    pygame.init()

    # Criar o objeto principal do jogo
    game = Game()

    # Iniciar o jogo
    game.run()

if __name__ == "__main__":
    main()
