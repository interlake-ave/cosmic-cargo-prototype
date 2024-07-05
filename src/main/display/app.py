"""Application classfile."""

import pygame
import pygame.constants as constant_type
import pygame.event as event_type
from constants import FPS, HEIGHT, WIDTH
from player.player import Player
from tilesets.platform import Platform

vec = pygame.math.Vector2


class App:
    """App class responsible for window and game loop."""

    def __init__(self) -> None:
        """Initialize the application window."""
        self._running = True
        self._display_surf = None
        self.size = (self.width, self.height) = (WIDTH, HEIGHT)

    def on_init(self) -> None:
        """Call pygame `pygame.init()`."""
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My-Game!")
        self.vec = pygame.math.Vector2
        self.FramesPerSecond = pygame.time.Clock()
        self._running = True
        self.player_1 = Player()
        self.platform = Platform()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player_1)
        self.all_sprites.add(self.platform)

    def on_event(self, event: event_type.Event) -> None:
        """Process events."""
        if event.type == constant_type.QUIT:
            self._running = False

    def on_loop(self) -> None:
        """Process game logic each game loop."""
        self.player_1.move()

    def on_render(self) -> None:
        """Process what to render each game loop."""
        self._display_surf.fill((0, 0, 0))

        for sprite in self.all_sprites.sprites():
            self._display_surf.blit(
                sprite.get_surf(),
                sprite.get_rect(),
            )

        pygame.display.update()
        self.FramesPerSecond.tick(FPS)

    def on_cleanup(self) -> None:
        """Clean up the game by calling `pygame.quit()`."""
        pygame.quit()

    def on_execute(self) -> None:
        """Run commands to execute by fetching events."""
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
