import pygame

pygame.init()
window = pygame.display.set_mode(size=(1024, 768))
print('Setup Start')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close Window
            quit()  # End pygame
