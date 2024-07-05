"""Application classfile."""

import pygame


class App:
    """App class responsible for window and game loop."""

    def __init__(self) -> None:
        """Initialize the application window."""
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self) -> None:
        """Call pygame `pygame.init()`."""
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._running = True

    def on_event(self, event: pygame.constants) -> None:
        """Process events."""
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self) -> None:
        """Process game logic each game loop."""
        pass

    def on_render(self) -> None:
        """Process what to render each game loop."""
        pass

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
