import pygame
import requests
import sys

ESP32_IP = "http://192.168.0.11/data"  # CAMBIA POR TU IP REAL

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Mando WiFi ESP32")
clock = pygame.time.Clock()

x, y = 400, 300
radius = 20
speed_factor = 3000

print("Conectado por WiFi")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    try:
        response = requests.get(ESP32_IP, timeout=0.05)
        data = response.text.strip()

        if "," in data:
            ax, ay, plus, minus = map(int, data.split(","))

            x += ax / speed_factor
            y -= ay / speed_factor

            if plus == 1:
                radius += 2
            if minus == 1:
                radius -= 2

    except:
        pass

    x = max(0, min(800, x))
    y = max(0, min(600, y))
    radius = max(5, min(200, radius))

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)