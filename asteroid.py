import pygame
import random
from constants import *
from circleshape import CircleShape

rand_num = random.uniform(20,50)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
       
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <+ ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = self.velocity.rotate(rand_num)
            neg_rand_angle = self.velocity.rotate(rand_num * -1)
            small_asteroid = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x,self.position.y,small_asteroid)
            asteroid_two = Asteroid(self.position.x,self.position.y,small_asteroid)
            asteroid_one.velocity = rand_angle * 1.2
            asteroid_two.velocity = neg_rand_angle *1.2