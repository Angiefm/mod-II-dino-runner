import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.small_cactus import SmallCactus

from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):    
        self.obstacles = []

    def generate_obstacle(self):
        obstacles_types = {
            0: SmallCactus(SMALL_CACTUS[0]),
            1: SmallCactus(SMALL_CACTUS[1]),
            2: SmallCactus(SMALL_CACTUS[2]),
            3: SmallCactus(LARGE_CACTUS[0]),
            4: SmallCactus(LARGE_CACTUS[1]),
            5: SmallCactus(LARGE_CACTUS[2]),
            6: Bird(BIRD[0])

        }

        return obstacles_types[random.randint(0,6)]

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.type == HAMMER_TYPE and game.player.dino_rect.colliderect(obstacle.rect):
                self.obstacles = []

            elif game.player.type == SHIELD_TYPE:
                print("...")

            elif game.player.dino_rect.colliderect(obstacle.rect):
                game.player.dead()
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 

    def remove_obstacles(self):
        self.obstacles = []