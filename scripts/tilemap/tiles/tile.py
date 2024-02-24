import pygame


class Tile:
    """tile super class"""
    def __init__(self, pos: tuple, size: int, settings):
        self.pos = pos
        self.size = size

        self.map_pos = (pos[0] * size, pos[1] * size)

        self.active_color = settings.main_mid
        self.inactive_color = settings.main_light

        self.player_color = settings.black_light

        self.border_color = settings.main_dark
        self.border_width = 2

        self.flag_id = 0
        self.flag_colors = (settings.white_light, settings.black_dark)

        self.color = self.active_color

        self._id = 0

        self.surf = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect(pos[0]*self.size, pos[1]*self.size, self.size, self.size)

        self.main_rect = pygame.Rect(0, 0, self.size, self.size)

        self.neighbours_ids = {
            1: -1, 2: -1, 3: -1,
            4: -1, 5: -1, 6: -1,
            7: -1, 8: -1, 9: -1,
        }
        self.bordering = "none"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        if value == 1:
            self.color = self.active_color
        elif value == 0:
            self.color = self.inactive_color
        elif value == 2:
            self.color = self.flag_colors[self.flag_id]
        elif value == 3:
            self.color = self.player_color

    def render(self, screen):
        self.draw_tile()
        self.draw_borders()
        screen.blit(self.surf, self.rect)

    def draw_borders(self):
        self.bordering = "none"
        if self._id == 1:
            if self.neighbours_ids[2] != 1 and self.neighbours_ids[2] != -1:  # top
                start_pos = (0, self.border_width//2.5)
                end_pos = (self.size, self.border_width//2.5)
                pygame.draw.line(self.surf, self.border_color, start_pos, end_pos, self.border_width)
                self.bordering = "top"
            if self.neighbours_ids[6] != 1 and self.neighbours_ids[6] != -1:  # right
                start_pos = (self.size-self.border_width, 0)
                end_pos = (self.size-self.border_width, self.size)
                pygame.draw.line(self.surf, self.border_color, start_pos, end_pos, self.border_width)
                self.bordering = "right"
            if self.neighbours_ids[8] != 1 and self.neighbours_ids[8] != -1:  # bottom
                start_pos = (self.size, self.size-self.border_width)
                end_pos = (0, self.size-self.border_width)
                pygame.draw.line(self.surf, self.border_color, start_pos, end_pos, self.border_width)
                self.bordering = "bottom"
            if self.neighbours_ids[4] != 1 and self.neighbours_ids[4] != -1:  # left
                start_pos = (0, self.size)
                end_pos = (0, 0)
                pygame.draw.line(self.surf, self.border_color, start_pos, end_pos, self.border_width)
                self.bordering = "left"

            if self.neighbours_ids[1] != 1 and self.neighbours_ids[1] != -1:  # topleft
                dot = pygame.Rect(0, 0, self.border_width, self.border_width)
                pygame.draw.rect(self.surf, self.border_color, dot)
            if self.neighbours_ids[3] != 1 and self.neighbours_ids[3] != -1:  # topright
                dot = pygame.Rect(
                    self.size-self.border_width, 0, self.border_width, self.border_width)
                pygame.draw.rect(self.surf, self.border_color, dot)
            if self.neighbours_ids[9] != 1 and self.neighbours_ids[9] != -1:  # bottomright
                dot = pygame.Rect(
                    self.size-self.border_width, self.size-self.border_width,
                    self.border_width, self.border_width)
                pygame.draw.rect(self.surf, self.border_color, dot)
            if self.neighbours_ids[7] != 1 and self.neighbours_ids[7] != -1:  # bottomleft
                dot = pygame.Rect(0, self.size-self.border_width, self.border_width, self.border_width)
                pygame.draw.rect(self.surf, self.border_color, dot)

    def draw_tile(self):
        pygame.draw.rect(self.surf, self.color, self.main_rect)
