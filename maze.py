from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()
fps = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()



x1 = 15
y1 = 420
x2 = 590
y2 = 275
x3 = 550
y3 = 400

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size1, player_size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2):
        super().__init__(player_image, player_x, player_y, player_speed, player_size1, player_size2)
        self.direction = 'left' #направление движения

    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 500:
            self.direction = 'right'
        if self.rect.x >= 630:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_heigth):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width #ширина
        self.height = wall_heigth #высота
        self.image = Surface((self.width, self.height)) #создание поверхности
        self.image.fill((self.color_1, self.color_2, self.color_3)) #заливка поверхности цветом
        self.rect = self.image.get_rect() #создание прямоугольника на основании поверхности
        self.rect.x = wall_x #координата x появления прямоугольника 
        self.rect.y = wall_y #координата y появления прямоугольника
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



hero = Player('hero.png', 15, 420, 5, 75,75)
cyborg = Enemy('cyborg.png', 500, 275, 2, 75,75)
treasure = GameSprite('treasure.png', 550, 400, 0, 75, 75)
wall1 = Wall(169, 255, 39, 110,50, 15,320)
wall2 = Wall(169, 255, 39, 110,35, 450,15)
wall3 = Wall(169, 255, 39, 110,470, 450,15)
wall4 = Wall(169, 255, 39, 215,150, 15,320)
wall5 = Wall(169, 255, 39, 340,50,  15,320)
wall6 = Wall(169, 255, 39, 450, 150, 15,320)
game = True
finish = False
money =  mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font.init()
font = font.SysFont('Arial', 70)
win = font.render('ТЫ ПОБЕДИЛ!', True, (255, 215, 0))
lose = font.render('ТЫ ПРОИГРАЛ:(', True, (255, 0, 0))
while game:
    keys_pressed = key.get_pressed()
    

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        hero.update()
        cyborg.reset()
        cyborg.update()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        if sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        


    display.update()
    clock.tick(fps)