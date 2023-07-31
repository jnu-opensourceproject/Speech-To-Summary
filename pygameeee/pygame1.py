import pygame

pygame.init()

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 
size = (400, 300)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

airplane = pygame.image.load('/Users/itaei/Desktop/pygameeee/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))


def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 20

        screen.blit(airplane, (x, y))
        pygame.display.update()

runGame()
pygame.quit()