import pygame


class Label:
    """this class handles and renders a label text to the screen"""
    def __init__(self, text: str, color, parent_surf, parent_rect):
        self.parent_surf = parent_surf
        self.parent_rect = parent_rect

        self._text = text.title()
        self.color = color

        self.font = pygame.font.Font(None, 32)
        self.margin = 8

        self.surf = self.font.render(self._text, True, self.color)
        self.rect = self.surf.get_rect()

        self._layout = ""
        self.layout = "top"

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, value):
        match value:
            case "top":
                self._layout = value
                self.rect.midtop = self.parent_rect.midtop
                self.rect.y += self.margin
            case "right":
                self._layout = value
                self.rect.midright = self.parent_rect.midright
                self.rect.x -= self.margin
            case "bottom":
                self._layout = value
                self.rect.midbottom = self.parent_rect.midbottom
                self.rect.y -= self.margin
            case "left":
                self._layout = value
                self.rect.midleft = self.parent_rect.midleft
                self.rect.x += self.margin
            case "center":
                self._layout = value
                self.rect.center = self.parent_rect.center
            case "topleft":
                self._layout = value
                self.rect.topleft = self.parent_rect.topleft
                self.rect.x += self.margin
                self.rect.y += self.margin
            case "topright":
                self._layout = value
                self.rect.topright = self.parent_rect.topright
                self.rect.x -= self.margin
                self.rect.y += self.margin
            case "bottomright":
                self._layout = value
                self.rect.bottomright = self.parent_rect.bottomright
                self.rect.x -= self.margin
                self.rect.y -= self.margin
            case "bottomleft":
                self._layout = value
                self.rect.bottomleft = self.parent_rect.bottomleft
                self.rect.x += self.margin
                self.rect.y -= self.margin

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value.title()
        self.surf = self.font.render(self._text, True, self.color)
        self.rect = self.surf.get_rect()
        self.layout = self._layout

    def render(self):
        self.parent_surf.blit(self.surf, self.rect)
