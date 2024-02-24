import pygame


class Scene:
    """scene class"""
    def __init__(self, main):
        self.main = main

        self.screen_size = (self.main.screen.get_width(), self.main.screen.get_height())

        self.surf = pygame.Surface((self.screen_size[0], self.screen_size[1]))
        self.rect = pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1])

        self.bg_color = self.main.settings.black_mid

        self.tile_size = self.main.settings.tile_size

    def run(self, dt):
        """scene run loop"""
        self.check_events()
        self.update_scene(dt)
        self.render_scene()

    def check_events(self):
        """event loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.running = False
            if event.type == pygame.KEYDOWN:
                self.key_pressed(event.key)
            if event.type == pygame.KEYUP:
                self.key_released(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicked(pygame.mouse.get_pressed())
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_released(pygame.mouse.get_pressed())

    def key_pressed(self, key):
        """handle key pressed events"""

    def key_released(self, key):
        """handle key released events"""

    def mouse_clicked(self, keys):
        """handle mouse clicked events"""

    def mouse_released(self, keys):
        """handle mouse released events"""

    def update_scene(self, dt):
        self.update(dt)

    def update(self, dt):
        """update game elements"""

    def render_scene(self):
        """render game elements"""
        self.surf.fill(self.bg_color)
        self.render()
        self.main.screen.blit(self.surf, self.rect)

    def render(self):
        """render scene elements"""
