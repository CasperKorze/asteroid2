import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    #CH2: Gameloop L3: Game Loop
    #Bez pygame.init() Pygame nie działa poprawnie.
    #To jest start całej biblioteki.
    pygame.init() 

    clock = pygame.time.Clock() #Ustawia zegar do kontrolowania klatek na sekundę
    dt = 0 #Delta time - czas między klatkami
    
    



    #Tworzy GUI window d;a gry
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Game loop
    running = True
    while running:
        log_state()

        for event in pygame.event.get():
            #Zamyka okno gry po kliknięciu na krzyżyk
            if event.type == pygame.QUIT:
                return
        #Tworzy czarny ekran na tyle
        screen.fill("black")
        # method to refresh the screen.
        pygame.display.flip() 
        dt = clock.tick(60) / 1000 #Ogranicza do 60 klatek na sekundę



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
