from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(random_angle)
        new_vel_2 = self.velocity.rotate(-random_angle)
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid_1.velocity = new_vel_1 * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid_2.velocity = new_vel_2 * 1.2