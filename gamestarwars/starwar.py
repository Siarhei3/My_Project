import pygame # Библиотека, управляет графикой звуком и т.д.
from gun import Gun # Подключаем класс Gun
import controls
from pygame.sprite import Group
from stats import Stats
from score import Scores



def run(): # все основыне функции и инициализацию  делаем в одной функции
    pygame.init()# инициализируем игру
    screen = pygame.display.set_mode((700,800)) # размер экрана
    pygame.display.set_caption("STAR WARS") # Название игры
    bg_color = (0, 0, 0) # Фоновый цвет RBG
    gun = Gun(screen) # Создаём объект пушки
    bullets = Group()
    inos = Group()
    controls.create_army(screen,inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True: # Запиываем в цикл все события в игре
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color,screen,stats, sc, gun, inos, bullets)
            controls.update_bullets(screen,stats,sc, inos,bullets)
            controls.update_inos(stats, screen,sc,  gun, inos, bullets)


run()