import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def split(self):
    if self.radius > ASTEROID_MIN_RADIUS:
      angle = random.uniform(20, 50)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      new_one = Asteroid(self.position.x, self.position.y, new_radius)
      new_one.velocity = self.velocity.rotate(angle) * 1.2
      new_two = Asteroid(self.position.x, self.position.y, new_radius)
      new_two.velocity = self.velocity.rotate(-angle) * 1.2
    self.kill()

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
