import random
import time
import pygame

class Die:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.original_image = pygame.image.load("textures/die_idle.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (size, size))
        self.image = self.original_image.copy()
        self.size = size
        self.rect = self.image.get_rect(topleft=(x, y))
        self.result = None
        self.font = pygame.font.SysFont(None, 60)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def roll(self):
        self.result = random.randint(1, 6)
        self.image = self.original_image.copy()
        text_surface = self.font.render(str(self.result), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        text_rect.x += 8
        text_rect.y += 8
        self.image.blit(text_surface, text_rect)
        print(f"Rolled: {self.result}")

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.roll()