import pygame
from class_ball import crear_sprite_circular

class Ranking():
    def __init__(self, previous_winners, actual_winner):

        nombre, victorias = list(actual_winner.items())[0]
        self.previous_winners = previous_winners
        self.actual_winner = (nombre, victorias)

    def draw(self, screen):
        font = pygame.font.Font("fonts/Coolvetica_font.otf", 60)
        bigger_font = pygame.font.Font("fonts/Coolvetica_font.otf", 120)

        pygame.draw.rect(screen, (0,0,0), (0, 0, 1920, 80))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 80, 1080))
        pygame.draw.rect(screen, (0, 0, 0), (1840, 0, 80, 1920))
        pygame.draw.rect(screen, (0, 0, 0), (0, 1000, 1920, 80))
        pygame.draw.rect(screen, (50, 50, 50), (50, 50, 1820, 980), border_radius= 20)

        background = pygame.image.load("sprites/background.jpg").convert()
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))

        tabla = pygame.image.load('sprites/final_ranking_image.png').convert_alpha()
        tabla = pygame.transform.scale(tabla, (600, 900))
        screen.blit(tabla, (1200, 100))

        tabla = pygame.image.load('sprites/final_champion_image.png').convert_alpha()
        tabla = pygame.transform.scale(tabla, (600, 900))
        screen.blit(tabla, (200, 100))

        previous_winners_text = []
        for winner in self.previous_winners:
            text = font.render(f'{winner} : {self.previous_winners[winner]}', True, (200, 200, 200))
            width = text.get_width()
            height = text.get_height()
            text = pygame.transform.smoothscale(text, (width * 1.4, height))
            previous_winners_text.append(text)

        y = 250
        for text in previous_winners_text:
            rect_text = text.get_rect(center=(1500, y))
            screen.blit(text, rect_text)
            y += 75


        winners_text = bigger_font.render(self.actual_winner[0], True, (240, 240, 240))
        width = winners_text.get_width()
        height = winners_text.get_height()
        winners_text = pygame.transform.smoothscale(winners_text, (width * 1.4, height))
        rect_text = winners_text.get_rect(center=(500, 450))
        screen.blit(winners_text, rect_text)

        sprite = crear_sprite_circular(self.actual_winner[1], 200)
        screen.blit(sprite, (400, 650))