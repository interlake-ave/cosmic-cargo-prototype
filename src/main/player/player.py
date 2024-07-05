"""Player main class file."""

import pygame
from constants import ACC, FRIC, HEIGHT, WIDTH
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    """Player main class."""

    def __init__(self) -> None:
        """Initialize the player sprite."""
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(15, 45))

        self.position = vec((10, 385))
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)

    def move(self) -> None:
        """Compute player movements."""
        self.acceleration = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acceleration.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acceleration.x = ACC
        if pressed_keys[K_UP]:
            self.acceleration.y = -ACC
        if pressed_keys[K_DOWN]:
            self.acceleration.y = ACC

        self.acceleration.x += self.velocity.x * FRIC
        self.acceleration.y += self.velocity.y * FRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH

        if self.position.y > HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = HEIGHT

        self.rect.midbottom = self.position

    def render(self, display_surface: pygame.Surface) -> None:
        """
        Render the sprite on the display.

        @args:
            displayer_surface: pygame.Surface
                The surface that the sprite get's rendered to.
        """
        display_surface.blit(self.get_surf(), self.get_rect())

    def get_surf(self) -> pygame.Surface:
        """
        The surface of the sprite.

        @returns
            pygame.Surface
                The sprite surface aka the sprite texture
        """
        return self.surf

    def get_rect(self) -> pygame.Rect:
        """
        The rectangle of the sprite.

        @returns
            pygame.Rect
                The rectangle of the sprite
        """
        return self.rect
