import pygame, pymunk, random



def crear_sprite_circular(ruta_imagen, diametro):
    bandera = pygame.image.load(ruta_imagen).convert_alpha()
    bandera = pygame.transform.scale(bandera, (diametro, diametro))

    superficie_final = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
    mascara = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
    pygame.draw.circle(mascara, (255, 255, 255, 255),
                        (diametro // 2, diametro // 2), diametro // 2)

    superficie_final.blit(bandera, (0, 0))
    superficie_final.blit(mascara, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    return superficie_final

class Ball():
    lista_objetos = []
    def __init__(self, space, pos, ruta_bandera, name):
        self.name = name
        self.radio = 20
        self.body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.body.velocity = (random.randint(25,100), random.randint(0,50))
        self.shape = pymunk.Circle(self.body, radius=self.radio)
        self.shape.collision_type = 1
        self.shape.elasticity = 0.9
        space.add(self.body, self.shape)
        self.sprite = crear_sprite_circular(ruta_bandera, self.radio * 2)
        Ball.lista_objetos.append(self)

    @classmethod
    def draw(self, screen, countries):
        for obj in Ball.lista_objetos:
            x, y = obj.body.position
            screen.blit(obj.sprite, (x - obj.radio, y - obj.radio))
        if len(Ball.lista_objetos) == 1:
            if len(countries[0]) == 1:
                font = pygame.font.SysFont('comicsans', 80)
                text = font.render(f'{Ball.lista_objetos[0].name} Won The Tournament', True, (0, 220, 0))
            else:
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(f'{Ball.lista_objetos[0].name} has been eliminated', True, (220, 0, 0))
            rect_text = text.get_rect()
            rect_text.center = (960, 200)
            screen.blit(text, rect_text)


