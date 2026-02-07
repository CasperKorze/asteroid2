import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    
    def rotate(self, dt):
        return dt * PLAYER_TURN_SPEED #Zmienna PLAYER_TURN_SPEED określa, jak szybko gracz będzie się obracał. Im większa wartość, tym szybszy obrót.
    

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= self.rotate(dt)
            
        if keys[pygame.K_d]:
            self.rotation += self.rotate(dt)
            


