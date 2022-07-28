from perlin import perlin, noise2D
import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Perlin Noise Visualizer")

octaves = 1

def drawNoise():
    for i in range(800):
        for j in range(600):
            value = int(noise2D(i,j,octaves) * 255)
            window.set_at((i, j), (value, value, value))
    pygame.display.update()

drawNoise()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                octaves += 1
                drawNoise()
            elif e.key == pygame.K_DOWN:
                octaves -= 1
                drawNoise()
            pygame.display.update()
