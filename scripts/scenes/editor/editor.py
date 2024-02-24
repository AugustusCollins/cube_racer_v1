import pygame
import json
import pathlib

from scripts.scenes.scene import Scene
from scripts.tilemap.tilemap import TileMap
from scripts.gui.label import Label


class Editor(Scene):
    """editor scene"""
    def __init__(self, main):
        super().__init__(main)

        self.grid_color = self.main.settings.black_light
        self.grid_surf = pygame.Surface(self.screen_size)
        self.grid_surf.set_colorkey("Black")

        self.tile_map = TileMap(self.screen_size, self.tile_size, self.main.settings)

        self.adding_tile = False
        self.adding_flag = False
        self.removing_tile = False

        self.start_pos = (0, 0)
        self.end_pos = (0, 0)

        self.selected = "ground"

        self.action_label = Label(self.selected, self.main.settings.white_light, self.surf, self.rect)
        self.action_label.layout = "topleft"

    def key_pressed(self, key):
        if key == pygame.K_w:
            self.to_world()
        elif key == pygame.K_s:
            self.action_label.text = "saved world"
            self.save_world()
        elif key == pygame.K_g:
            action = "ground"
            self.action_label.text = action
            self.selected = action
        elif key == pygame.K_f:
            action = "flag"
            self.action_label.text = action
            self.selected = action
        elif key == pygame.K_p:
            action = "player"
            self.action_label.text = action
            self.selected = action

    def mouse_clicked(self, keys):
        if keys[0]:
            if self.selected == "ground":
                self.removing_tile = True
                self.start_pos = pygame.mouse.get_pos()
            elif self.selected == "flag":
                self.adding_flag = True
                self.start_pos = pygame.mouse.get_pos()
            elif self.selected == "player":
                self.tile_map.add_player(pygame.mouse.get_pos())
        if keys[2]:
            self.adding_tile = True
            self.start_pos = pygame.mouse.get_pos()

    def mouse_released(self, keys):
        if not keys[0]:
            if self.removing_tile:
                self.removing_tile = False
                self.end_pos = pygame.mouse.get_pos()
                self.tile_map.remove_tiles(self.start_pos, self.end_pos)
            elif self.adding_flag:
                self.adding_flag = False
                self.end_pos = pygame.mouse.get_pos()
                self.tile_map.add_flags(self.start_pos, self.end_pos)
        if not keys[2] and self.adding_tile:
            self.adding_tile = False
            self.end_pos = pygame.mouse.get_pos()
            self.tile_map.add_tiles(self.start_pos, self.end_pos)

    def save_world(self):
        world = {}
        for tile, value in self.tile_map.tile_dict.items():
            world[str(tile)] = [value.id, value.flag_id]

        path = pathlib.Path("worlds/worlds.json")
        contents = json.dumps(world)
        path.write_text(contents)

    def to_world(self):
        self.main.to_world()

    def render(self):
        self.tile_map.render(self.surf)
        self.draw_grid()
        self.draw_indicator()
        self.action_label.render()

    def draw_grid(self):
        """render grid to screen"""
        col_amount = self.screen_size[0] // self.tile_size
        row_amount = self.screen_size[1] // self.tile_size

        # draw columns
        for count in range(col_amount + 1):
            x_pos = count * self.tile_size
            pygame.draw.line(self.grid_surf, self.grid_color, (x_pos, 0), (x_pos, self.screen_size[1]))

        # draw rows
        for count in range(row_amount + 1):
            y_pos = count * self.tile_size
            pygame.draw.line(self.grid_surf, self.grid_color, (0, y_pos), (self.screen_size[0], y_pos))

        self.surf.blit(self.grid_surf, (0, 0))

    def draw_indicator(self):
        if self.removing_tile or self.adding_tile or self.adding_flag:
            current_pos = pygame.mouse.get_pos()
            line_color = self.main.settings.white_light

            top_line = [self.start_pos, (current_pos[0], self.start_pos[1])]
            right_line = [(current_pos[0], self.start_pos[1]), current_pos]
            bottom_line = [(self.start_pos[0], current_pos[1]), current_pos]
            left_line = [self.start_pos, (self.start_pos[0], current_pos[1])]

            pygame.draw.line(self.surf, line_color, top_line[0], top_line[1])
            pygame.draw.line(self.surf, line_color, right_line[0], right_line[1])
            pygame.draw.line(self.surf, line_color, bottom_line[0], bottom_line[1])
            pygame.draw.line(self.surf, line_color, left_line[0], left_line[1])
