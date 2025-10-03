from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random as rand

class Asteroid(CircleShape):
    def __init__(self,x ,y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = rand.uniform(20,50)
            first_vec = self.velocity.rotate(random_angle)
            second_vec = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_child = Asteroid(self.position[0],self.position[1],new_radius)
            second_child = Asteroid(self.position[0],self.position[1],new_radius)

            first_child.velocity = first_vec*1.2
            second_child.velocity = second_vec*1.2
