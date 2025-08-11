from constants import *
from player import Player
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    # Drawing the game onto the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        player.draw(screen)
        pygame.display.flip()
    clock.tick(60)

    dt = clock.tick.get_time() / 1000
    return dt

    Player()


if __name__ == "__main__":
    main()
