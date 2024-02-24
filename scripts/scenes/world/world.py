import pygame
import json
import pathlib

from scripts.scenes.scene import Scene
from scripts.tilemap.tilemap import TileMap
from scripts.player.cube import Cube


class World(Scene):
    """world-class"""
    def __init__(self, main):
        super().__init__(main)

        self.tile_map = TileMap(self.screen_size, self.tile_size, self.main.settings)

        self.cubes = []

    def set_world(self):
        path = pathlib.Path("worlds/worlds.json")
        if path.exists():
            contents = path.read_text()
            new_world = json.loads(contents)
            self.tile_map.set_world_tiles(new_world)
        self.set_players()

    def set_players(self):
        num = 0
        self.cubes.clear()
        for tile in self.tile_map.tile_dict.values():
            if tile.id == 3:
                tile.id = 0
                cube = Cube(
                    (tile.pos[0]*self.tile_size, tile.pos[1]*self.tile_size),
                    num,
                    self.tile_map.tile_dict,
                    self.main.settings,
                    self.surf,
                    self.rect
                )
                self.cubes.append(cube)
                num += 1
                num %= 4

    def key_pressed(self, key):
        if key == pygame.K_e:
            self.to_editor()

    def to_editor(self):
        self.main.to_editor()

    def update(self, dt):
        self.update_players(dt)

    def update_players(self, dt):
        for cube in self.cubes:
            cube.update(dt)

    def render(self):
        self.tile_map.render(self.surf)
        self.render_players()

    def render_players(self):
        for cube in self.cubes:
            cube.render()
