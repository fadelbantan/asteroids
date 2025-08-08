from constants import *
import pygame



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock
    dt = 0
    # GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # "Drawing the game onto the screen"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        pygame.display.flip()
    clock.tick(60)

    dt = clock.tick.get_time() / 1000
    return dt


if __name__ == "__main__":
    main()
