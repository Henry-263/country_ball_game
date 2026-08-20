import pygame
from class_ball import crear_sprite_circular

class Ranking():

    def __init__(self, previous_winners, actual_winner):

        self.font = pygame.font.Font("fonts/Coolvetica_font.otf", 60)
        self.bigger_font = pygame.font.Font("fonts/Coolvetica_font.otf", 120)

        nombre, victorias = list(actual_winner.items())[0]
        self.previous_winners = previous_winners
        self.actual_winner = (nombre, victorias)
        self.inicial_position = [0, -1920]

        self.background = pygame.image.load("sprites/Flag-map_of_the_world.png").convert()
        self.background = pygame.transform.smoothscale(self.background, (1920, 1080))

        self.tabla = pygame.image.load('sprites/final_champion_image.png').convert_alpha()
        self.tabla = pygame.transform.scale(self.tabla, (600, 900))

        self.tabla2 = pygame.image.load('sprites/final_ranking_image.png').convert_alpha()
        self.tabla2 = pygame.transform.scale(self.tabla2, (600, 900))

        self.previous_winners_text = []
        for winner in self.previous_winners:
            text = self.font.render(f'{winner} : {self.previous_winners[winner]}', True, (200, 200, 200))
            width = text.get_width()
            height = text.get_height()
            text = pygame.transform.smoothscale(text, (width * 1.4, height))
            self.previous_winners_text.append(text)

        self.winners_text = self.bigger_font.render(self.actual_winner[0], True, (240, 240, 240))
        width = self.winners_text.get_width()
        height = self.winners_text.get_height()
        self.winners_text = pygame.transform.smoothscale(self.winners_text, (width * 1.4, height))

        self.sprite = crear_sprite_circular(self.actual_winner[1], 200)




    def draw(self, screen):
        screen.blit(self.background, (self.inicial_position[0], 0))
        screen.blit(self.background, (self.inicial_position[1], 0))

        self.inicial_position = [x + 1 for x in self.inicial_position]

        if self.inicial_position[0] >= 1920:
            self.inicial_position[0] = self.inicial_position[1] - 1920

        if self.inicial_position[1] >= 1920:
            self.inicial_position[1] = self.inicial_position[0] - 1920

        screen.blit(self.tabla2, (1200, 100))

        screen.blit(self.tabla, (200, 100))

        y = 250
        for text in self.previous_winners_text:
            rect_text = text.get_rect(center=(1500, y))
            screen.blit(text, rect_text)
            y += 75

        rect_text = self.winners_text.get_rect(center=(500, 450))
        screen.blit(self.winners_text, rect_text)

        screen.blit(self.sprite, (400, 650))