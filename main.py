import pygame, pymunk, sys, json, random
from class_ball import Ball
from class_wall import Wall

def create_world(space):
    if Wall.lista_objetos:
        for wall in Wall.lista_objetos:
            space.remove(wall.shape, wall.body)
            Wall.lista_objetos.remove(wall)

    # Crear muros: (posicion), grosor, altura, angulo, kill
    levels = [
        {
        1:[(960, 1030), 200, 100, 0, True],
        2: [(25, 540), 50, 1080, 0, False],
        3:[(400, 600), 50, 1080, -60, False],
        4:[(1895, 540), 50, 1080, 0, False],
        5:[(1520, 600), 50, 1080, 60, False],
        6:[(855, 973), 50, 250, 0, False],
        7:[(1064, 973), 50, 250, 0, False],
        },
        {
        1: [(960, 1030), 1820, 100, 0, True],
        2: [(25, 540), 50, 1080, 0, False],
        3: [(1895, 540), 50, 1080, 0, False],
        4: [(450, 300), 900, 50, 20, False],
        5: [(1470, 300), 900, 50, -20, False],
        6: [(450, 650), 900, 50, 20, False],
        7: [(1470, 650), 900, 50, -20, False],
        8: [(960, 1150), 2000, 50, 0, True],
        }
    ]

    #level = random.randint(0, len(levels) - 1)
    level = 1

    for num in levels[level]:
            Wall(space, levels[level][num][0], levels[level][num][1], levels[level][num][2], levels[level][num][3], levels[level][num][4])

def eliminar_obj(arbiter, space, data):

    bola_shape, muro_shape = arbiter.shapes

    # Busca el objeto Ball correspondiente a ese shape y llama a su metodo
    for obj in Ball.lista_objetos:
        if obj.shape == bola_shape:
            space.remove(obj.shape, obj.body)
            Ball.lista_objetos.remove(obj)
            break
    return True

def spawn_balls(space, countries):

    i = 0
    for country in countries[0]:
        Ball(space, (50*i+250, 50), countries[0][country], country)
        i += 1
    return i


def last_ball(balls_num, tiempo):
    if len(Ball.lista_objetos) == 1:
        for obj in Wall.lista_objetos:
            if obj.shape.collision_type == 2:
                obj.shape.collision_type = 4
                return balls_num - 1, pygame.time.get_ticks()
    return balls_num, tiempo

if __name__ == "__main__":

    with open('balls.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)

    pygame.init()
    screen = pygame.display.set_mode((1920,1080))  # La pantalla
    pygame.display.set_caption("Last Countrie's Standing")
    clock = pygame.time.Clock()   #Controlar los FPS
    font = pygame.font.SysFont("comicsans", 30)

    space = pymunk.Space()
    space.gravity = 0.0, 100.0

    finish_game = True
    tiempo = None
    space.on_collision(collision_type_a=1, collision_type_b=2, begin=eliminar_obj)
    while True:
        if finish_game:
            balls_num = spawn_balls(space, countries)
            create_world(space)
            finish_game = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        balls_num, tiempo  = last_ball(balls_num, tiempo)

        if tiempo and (pygame.time.get_ticks() - tiempo >= 3000) and len(countries[0]) > 1:
            tiempo = None
            finish_game = True
            del countries[0][(Ball.lista_objetos[0].name)]
            space.remove(Ball.lista_objetos[0].shape, Ball.lista_objetos[0].body)
            Ball.lista_objetos.remove(Ball.lista_objetos[0])


        screen.fill((50,50,50))  # Rellenamos la pantalla de negro
        Ball.draw(screen, countries)
        Wall.draw(screen)

        space.step(1/50)
        pygame.display.flip()
        clock.tick(165)



