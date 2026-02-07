import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    #CH2: Gameloop L3: Game Loop
    #Bez pygame.init() Pygame nie działa poprawnie.
    #To jest start całej biblioteki.
    pygame.init() 

    #Tworzy grupy sprite'ów do aktualizacji i rysowania
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    


    clock = pygame.time.Clock() #Ustawia zegar do kontrolowania klatek na sekundę
    dt = 0 #Delta time - czas między klatkami
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #Tworzy gracza na środku ekranu
    updatable.update(dt) #Aktualizuje gracza (np. jego pozycję, rotację itp.) na podstawie delta time



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
            
        dt = clock.tick(60) / 1000 #Ogranicza do 60 klatek na sekundę
        updatable.update(dt) #Aktualizuje gracza (np. jego pozycję, rotację itp.) na podstawie delta time

    
    


        #Tworzy czarny ekran na tyle
        screen.fill("black")
        # method to refresh the screen.
        player.draw(screen) #Rysuje gracza na ekranie

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip() 
    

    



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
