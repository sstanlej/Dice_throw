import sys
import pygame
from dice import Die

SCREEN_WIDTH, SCREEN_HIGHT = 800, 500
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption("Dice thrower")
    clock = pygame.time.Clock()

    image_bg1 = pygame.image.load("textures/background1.png")
    image_bg1 = pygame.transform.scale(image_bg1, (800, 500))

    die1 = Die(200, 200, 100)

    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                die1.handle_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.blit(image_bg1, (0, 0))
        die1.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()