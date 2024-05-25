import pygame
import math
import time

pygame.init()
pygame.font.init()

fontfile = "Ubuntu-B.ttf"

font = pygame.font.Font(fontfile, 13)

WIDTH, HEIGHT = 1000, 1000
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
BROWN = (165, 42, 42)
GRAY = (169, 169, 169)

FPS = 60
speed_modifier = 0
running = True
labels = False
label_toggle_cooldown = 4
last_label_toggle = 0

s = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

clock = pygame.time.Clock()

class Planet:
    def __init__(self, name, colour, radius, distance, speed):
        self.name = name
        self.colour = colour
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.angle = 0
    def update_position(self):
        global speed_modifier
        self.angle += self.speed + speed_modifier
        if self.angle >= 360:
            self.angle -= 360
        x = WIDTH//2+self.distance*math.cos(math.radians(self.angle))
        y = HEIGHT//2+self.distance*math.sin(math.radians(self.angle))
        return (int(x), int(y))
    def draw_name(self):
        x = WIDTH//2+self.distance*math.cos(math.radians(self.angle))
        y = HEIGHT//2+self.distance*math.sin(math.radians(self.angle))
        if self.name == "Sun":
            pass
        else:
            s.blit(font.render(self.name, 1, WHITE), (x- 20, y+2))




sun = Planet("Sun", YELLOW, 40, 0,0)
mercury = Planet("Mercury", GRAY, 5, 60, 0.24)
venus = Planet("Venus", ORANGE, 7, 100, 0.18)
earth = Planet("Earth", BLUE, 10, 150, 0.12)
mars = Planet("Mars", RED, 8, 200, 0.1)
jupiter = Planet("Jupiter", ORANGE, 20, 250, 0.05)
saturn = Planet("Saturn", BROWN, 17, 300, 0.04)
uranus = Planet("Uranus", LIGHT_BLUE, 14, 350, 0.03)
neptune = Planet("Neptune", BLUE, 13, 400, 0.02)

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def update_screen():
    global speed_modifier, labels
    s.fill(BLACK)
    for p in planets:
        if p == sun:
            position = (WIDTH//2, HEIGHT//2)
        else:
            position = p.update_position()
        pygame.draw.circle(s, p.colour, position, p.radius)
        if labels:
            p.draw_name()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        speed_modifier += 0.01
    if keys[pygame.K_t]:
        current_time = time.time()
        if current_time - last_label_toggle > label_toggle_cooldown:
            if labels == True:
                labels = False
            else:
                labels = True
            last_label_toggle_time = current_time

    s.blit(font.render("Press 's' to speed up",1, WHITE), (10, 28))
    text = "FPS = "
    text += str(round(clock.get_fps()))
    s.blit(font.render(text, 1, WHITE), (10, 10))
    s.blit(font.render("Press 't' to toggle labels", 1, WHITE), (10, 46))
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update_screen()
    clock.tick(FPS)


