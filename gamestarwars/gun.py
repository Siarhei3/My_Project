import pygame
from pygame.sprite import Sprite

class Gun(Sprite): # Всю логику которая косается оружия содержится в классе GUN
    def __init__(self, screen): # Метод инициализации будет принимать графический объект
        """Инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen # Получаем наш экран
        self.image = pygame.image.load('image/tank.png') # Загружаем изображения нашей пушки
        self.rect = self.image.get_rect()# Берем как прямоугольник наше изображение и расположем пушку на графическом
        # объекте rect - прямоугольник
        self.screen_rect = screen.get_rect() # получаем объект экрана в качестве прямоугольника
        self.rect.centerx = self.screen_rect.centerx # Координата нашей пушки по центру
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom # Нижняя координата пушки
        self.mright = False
        self.mleft = False

    def output(self): # Выводим на экран
        """Рисование пушки"""
        self.screen.blit(self.image, self.rect) # Метод blit отрисовывает пушку

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center +=1.5

        if self.mleft and self.rect.left > 0:
            self.center -=1.5

        self.rect.centerx = self.center

    def create_gun(self): # размещаем пушку внизу
        self.center = self.screen_rect.centerx

