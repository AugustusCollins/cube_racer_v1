import pygame


class Cube:
    """player cube class"""
    def __init__(self, pos: tuple, num, tile_dict, settings, parent_surf, parent_rect, start_dir="random"):
        self.parent_surf = parent_surf
        self.parent_rect = parent_rect

        self.tile_dict = tile_dict
        self.settings = settings

        self.size = settings.tile_size * 1.5

        self.speed = 100
        self.direction = self.set_start_dir(start_dir)

        self.surf = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect(pos[0], pos[1], self.size, self.size)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving = True
        self.color, self.br_color = self.set_color(num)

        self.on_wall = False

    def set_color(self, num):
        match num:
            case 0:
                color = self.settings.main_light
                br_color = self.settings.main_mid
            case 1:
                color = self.settings.red_light
                br_color = self.settings.red_mid
            case 2:
                color = self.settings.green_light
                br_color = self.settings.green_mid
            case _:
                color = self.settings.blue_light
                br_color = self.settings.blue_mid
        return color, br_color

    @staticmethod
    def set_start_dir(direction: str):
        vector = [0.5, 0.5]

        match direction:
            case "up":
                vector = [0, -1]
            case "right":
                vector = [1, 0]
            case "down":
                vector = [0, 1]
            case "left":
                vector = [-1, 0]

        return vector

    def update(self, dt):
        self.wall_collision()
        self.move(dt)

    def wall_collision(self):
        for tile in self.tile_dict.values():
            if tile.bordering != "none":
                if self.rect.colliderect(tile.rect):
                    self.direction[0] = -self.direction[0]
                    self.direction[1] = -self.direction[1]

    def move(self, dt):
        if self.moving:
            self.x += self.direction[0] * self.speed * dt
            self.y += self.direction[1] * self.speed * dt

        self.rect.x = self.x
        self.rect.y = self.y

    def render(self):
        self.draw_cube()
        self.parent_surf.blit(self.surf, self.rect)

    def draw_cube(self):
        self.surf.fill(self.color)
        border_rect = pygame.Rect(0, 0, self.size, self.size)
        pygame.draw.rect(self.surf, self.br_color, border_rect, width=2)
