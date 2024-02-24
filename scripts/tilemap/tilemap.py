import pygame
import math

from scripts.tilemap.tiles.tile import Tile


class TileMap:
    """tile map class"""
    def __init__(self, screen_size: tuple, tile_size: int, settings):
        self.screen_size = screen_size
        self.settings = settings

        self.surf = pygame.Surface(self.screen_size)
        self.rect = pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1])

        self.tile_size = tile_size
        self.tile_dict = self.set_tile_dict()

    def set_tile_dict(self):
        """set tile dictionary according to screen size"""
        tile_dict = {}

        cols = math.ceil(self.screen_size[0] / self.tile_size)
        rows = math.ceil(self.screen_size[1] / self.tile_size)

        for x in range(cols):
            for y in range(rows):
                new_tile = Tile((x, y), self.tile_size, self.settings)
                new_tile.id = 1
                tile_dict[(x, y)] = new_tile

        return tile_dict

    def set_tile_neighbours(self):
        """set tile neighbours id"""
        neighbours_offset = {
            1: (-1, -1), 2: (0, -1), 3: (+1, -1),
            4: (-1, 0), 5: (0, 0), 6: (+1, 0),
            7: (-1, +1), 8: (0, +1), 9: (+1, +1),
        }

        for tile in self.tile_dict.values():
            if tile.id == 1:
                for neighbour in tile.neighbours_ids.keys():
                    neighbor_pos = (
                        tile.pos[0]+neighbours_offset[neighbour][0],
                        tile.pos[1]+neighbours_offset[neighbour][1]
                    )
                    if self.tile_dict.get(neighbor_pos):
                        neighbour_id = self.tile_dict[neighbor_pos].id
                        tile.neighbours_ids[neighbour] = neighbour_id

    def set_world_tiles(self, world_dict: dict):
        for tile, value in world_dict.items():
            self.tile_dict[eval(tile)].flag_id = value[1]
            self.tile_dict[eval(tile)].id = value[0]
        self.set_tile_neighbours()

    def tile_start_end_pos(self, pos_1, pos_2):
        start_pos = [min(pos_1[0], pos_2[0]), min(pos_1[1], pos_2[1])]
        end_pos = [max(pos_1[0], pos_2[0]), max(pos_1[1], pos_2[1])]

        tile_start_pos = (start_pos[0] // self.tile_size, start_pos[1] // self.tile_size)
        tile_end_pos = (end_pos[0] // self.tile_size, end_pos[1] // self.tile_size)

        return tile_start_pos, tile_end_pos

    def add_tiles(self, pos_1, pos_2):
        """set tile in tile dictionary to 1"""
        tile_start_pos, tile_end_pos = self.tile_start_end_pos(pos_1, pos_2)

        for x in range(tile_start_pos[0], tile_end_pos[0] + 1):
            for y in range(tile_start_pos[1], tile_end_pos[1] + 1):
                if self.tile_dict.get((x, y)):
                    self.tile_dict[(x, y)].id = 1

        self.set_tile_neighbours()

    def remove_tiles(self, pos_1, pos_2):
        """set tile in tile dictionary to 0"""
        tile_start_pos, tile_end_pos = self.tile_start_end_pos(pos_1, pos_2)

        for x in range(tile_start_pos[0], tile_end_pos[0] + 1):
            for y in range(tile_start_pos[1], tile_end_pos[1] + 1):
                if self.tile_dict.get((x, y)):
                    self.tile_dict[(x, y)].id = 0

        self.set_tile_neighbours()

    def add_flags(self, pos_1, pos_2):
        """set tile_id in tile dictionary to 2"""
        tile_start_pos, tile_end_pos = self.tile_start_end_pos(pos_1, pos_2)

        current_flag_id = 0
        for x in range(tile_start_pos[0], tile_end_pos[0] + 1):
            for y in range(tile_start_pos[1], tile_end_pos[1] + 1):
                if self.tile_dict.get((x, y)):
                    self.tile_dict[(x, y)].flag_id = current_flag_id
                    self.tile_dict[(x, y)].id = 2
                    current_flag_id += 1
                    current_flag_id %= 2

        self.set_tile_neighbours()

    def add_player(self, pos):
        tile_pos = (pos[0] // self.tile_size, pos[1] // self.tile_size)
        if self.tile_dict.get(tile_pos):
            self.tile_dict[tile_pos].id = 3

    def render(self, ps):
        self.render_tiles()

        ps.blit(self.surf, self.rect)

    def render_tiles(self):
        for tile, value in self.tile_dict.items():
            value.render(self.surf)
