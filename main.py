import pygame, pymunk, sys, json, random
from class_ball import Ball
from class_wall import Wall, Moving_Wall
from levels import return_levels

def create_world(space):
    if Wall.lista_objetos:
        for wall in Wall.lista_objetos:
            space.remove(wall.shape, wall.body)
        Wall.lista_objetos.clear()

    # Crear muros: (posicion), grosor, altura, angulo, kill
    levels = return_levels()

    #level = random.randint(0, len(levels) - 1)
    level = 6

    for num in levels[level]:
        if isinstance(num, int):
            Wall(space, levels[level][num][0], levels[level][num][1], levels[level][num][2], levels[level][num][3], levels[level][num][4], levels[level][num][5])
        else:
            Moving_Wall(space, levels[level][num][0], levels[level][num][1], levels[level][num][2], levels[level][num][6], levels[level][num][7], levels[level][num][8], levels[level][num][3], levels[level][num][4], levels[level][num][5])

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
    aux_countries = list(countries[0].items())
    random.shuffle(aux_countries)
    x = True
    for country in aux_countries:
        if x:
            Ball(space, (50*i+100, 50), country[1], country[0])
        else:
            Ball(space, (50*i+100, 100), country[1], country[0])
        i += 1
        if i > 30:
            i = 0
            x = False
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

        Moving_Wall.move_walls()
        Ball.draw(screen, countries)
        Wall.draw(screen)
        space.step(1/50)
        pygame.display.flip()
        clock.tick(165)



