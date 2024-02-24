import pygame
import sys

from scripts.settings.settings import Settings
from scripts.scenes.editor.editor import Editor
from scripts.scenes.world.world import World


class Main:
    """main class"""
    def __init__(self):
        """initialize game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((360, 640))
        pygame.display.set_caption("Cube Racer")

        self.clock = pygame.time.Clock()
        self.running = True

        self.settings = Settings()
        self.bg_color = self.settings.black_dark

        self.mode = "editor"
        self.editor = Editor(self)
        self.world = World(self)

    def run(self):
        """main game loop"""
        while self.running:
            dt = self.clock.tick() / 1000
            self.screen.fill(self.bg_color)

            if self.mode == "editor":
                self.editor.run(dt)
            elif self.mode == "world":
                self.world.run(dt)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def to_world(self):
        self.world.set_world()
        self.mode = "world"

    def to_editor(self):
        self.mode = "editor"
        self.editor.action_label.text = self.editor.selected


if __name__ == "__main__":
    Main().run()
