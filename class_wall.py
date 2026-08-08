import pygame, pymunk, sys
from math import radians


class Wall():
    lista_objetos = []
    def __init__(self, space, pos, width, height, angle=0, kill = False):
        self.angle = angle
        self.width = width
        self.height = height
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.body.angle = radians(angle)
        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.elasticity = 0.9
        if kill:
            self.shape.collision_type = 2
        else:
            self.shape.collision_type = 3
        space.add(self.body, self.shape)
        Wall.lista_objetos.append(self)

    @classmethod
    def draw(self, screen):
        for obj in Wall.lista_objetos:
            vertices = obj.shape.get_vertices()
            puntos = [obj.body.local_to_world(v) for v in vertices]
            puntos = [(int(p.x), int(p.y)) for p in puntos]
            if obj.shape.collision_type == 2:
                pygame.draw.polygon(screen, (0, 220, 0), puntos)
            elif obj.shape.collision_type == 3:
                pygame.draw.polygon(screen, (150, 150, 150), puntos)
            else:
                pygame.draw.polygon(screen, (220, 0, 0), puntos)