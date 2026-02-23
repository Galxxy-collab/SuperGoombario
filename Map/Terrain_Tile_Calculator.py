import pygame, csv, os
camera_x_offset = 0
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 64
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface, camera_x_offset):
        surface.blit(self.map_surface, (camera_x_offset, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '100':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '0':
                    tiles.append(Tile('left_angle_plot.png', self.spritesheet))
                elif tile == '1':
                    tiles.append(Tile('middle_angle_plot.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('right_angle_plot.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '8':
                    tiles.append(Tile('left_middle_plot.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '9':
                    tiles.append(Tile('middle_plot.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '10':
                    tiles.append(Tile('right_middle_plot.png', x * self.tile_size, y * self.tile_size, self.spritesheet))



                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles









