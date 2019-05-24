import pygame
import os

directory = 'images'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

Textures = dict()

for image in images:
    name = image[0:-4]
    Textures[name] = pygame.image.load(os.path.join(directory, image))

print(Textures)



