import pygame
# inicializando o mixer do pygame 
pygame.init()
pygame.mixer.init()
# chamando a musica 
pygame.mixer.music.load('ex001.mp3')
#play na musica
pygame.mixer.music.play()
input()
pygame.event.wait() 

