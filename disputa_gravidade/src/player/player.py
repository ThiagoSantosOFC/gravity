# src/player/__init__.py

import pygame

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.x, self.y = 100, 100
        self.width, self.height = 50, 50
        self.color = (255, 0, 0) if player_id == 1 else (0, 0, 255)
        self.velocity = 5
        self.gravity_direction = (0, 1)  # Downward gravity initially
        self.is_gravity_frozen = False
        self.is_control_inverted = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.toggle_gravity('up')
            elif event.key == pygame.K_s:
                self.toggle_gravity('down')
            elif event.key == pygame.K_a:
                self.toggle_gravity('left')
            elif event.key == pygame.K_d:
                self.toggle_gravity('right')
            elif event.key == pygame.K_SPACE:
                self.activate_special_power()

    def toggle_gravity(self, direction):
        if not self.is_gravity_frozen:
            if direction == 'up':
                self.gravity_direction = (0, -1)
            elif direction == 'down':
                self.gravity_direction = (0, 1)
            elif direction == 'left':
                self.gravity_direction = (-1, 0)
            elif direction == 'right':
                self.gravity_direction = (1, 0)

    def activate_special_power(self):
        # Placeholder for special power activation logic
        pass

    def update(self):
        if self.is_gravity_frozen:
            return
        
        self.x += self.velocity * self.gravity_direction[0]
        self.y += self.velocity * self.gravity_direction[1]

        self.rect.topleft = (self.x, self.y)

    def render(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)

    def has_won(self):
        
        if self.rect.colliderect(pygame.Rect(500, 500, 50, 50)):
            return True
