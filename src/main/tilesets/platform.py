"""Platform main class file."""

import pygame
from constants import HEIGHT, WIDTH


class Platform(pygame.sprite.Sprite):
    """Platform main class."""

    def __init__(self) -> None:
        """Initialize the platform at the bottom of the screen."""
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))

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
