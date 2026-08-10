import pygame, pymunk, sys
from math import radians


class Wall():
    lista_objetos = []
    def __init__(self, space, pos, width, height, angle=0, kill = False, polig = 'Rectangle'):
        self.pos = pos
        self.polig = polig
        self.angle = angle
        self.width = width
        self.height = height
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = pos
        self.body.angle = radians(angle)
        if self.polig == 'Circle':
            self.shape = pymunk.Circle(self.body, radius=self.width)
        else:
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
            if obj.polig == 'Circle':
                pygame.draw.circle(screen, (150, 150,150), obj.body.position, obj.shape.radius)
            else:
                vertices = obj.shape.get_vertices()
                puntos = [obj.body.local_to_world(v) for v in vertices]
                puntos = [(int(p.x), int(p.y)) for p in puntos]
                if obj.shape.collision_type == 2:
                    pygame.draw.polygon(screen, (0, 220, 0), puntos)
                elif obj.shape.collision_type == 3:
                    pygame.draw.polygon(screen, (150, 150, 150), puntos)
                else:
                    pygame.draw.polygon(screen, (220, 0, 0), puntos)

class Moving_Wall(Wall):
    lista_objetos = []
    def __init__(self, space, pos, width, height, final_pos_r, final_pos_l, vel, angle=0, kill = False, polig = 'Rectangle'):
        Wall.__init__(self, space, pos, width, height, angle, kill, polig)
        self.final_pos_r = final_pos_r
        self.final_pos_l = final_pos_l
        self.vel = vel
        Moving_Wall.lista_objetos.append(self)

    @classmethod
    def move_walls(self):
        for obj in Moving_Wall.lista_objetos:
            if (obj.body.position[0] >= obj.final_pos_r[0] and obj.vel > 0) or (obj.body.position[0] <= obj.final_pos_l[0] and obj.vel < 0):
                obj.vel *= -1
            obj.body.velocity = (obj.vel, 0)
            if obj.angle:
                obj.body.angle += radians(obj.angle)