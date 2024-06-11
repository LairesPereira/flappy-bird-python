import random
import pygame

surface = pygame.Surface((100, 100), pygame.SRCALPHA)
image = pygame.image.load("imgs/bird1.png")
image_bg = pygame.image.load("imgs/bg.png")
image_pipe = pygame.image.load("imgs/pipe.png")
game_over_img = pygame.image.load("imgs/game_over.png")

pygame.init()
screen = pygame.display.set_mode((288, 512))
game_over = False
done = False
going_up = False
going_up_count = 0
clock = pygame.time.Clock()
bird_pos_x = 90
bird_pos_y = 100
pipe_down_pos_x = 238
pipe_down_pos_y = 450
pipe_up_pos_x = 238
pipe_up_pos_y = -100
pipe_max_pos_y = 200
pipe_min_pos_y = 450

while not done:
    if game_over:
        screen.fill((255, 255, 255))
        screen.blit(image_bg, (0, 0))
        screen.blit(pygame.transform.scale(game_over_img, (200, 100)), (45, 200))
        pygame.display.flip()
        pygame.time.delay(3000)
        exit(1)

    if pipe_down_pos_x < -53:
        pipe_down_pos_x = 288
        pipe_up_pos_x = 288
        pipe_down_pos_y = random.randint(pipe_max_pos_y, pipe_min_pos_y)
        pipe_up_pos_y =  -320 + (random.randint(0, 256))
        if((pipe_down_pos_y + (pipe_up_pos_y * -1)) < 470):
            pipe_up_pos_y -= 90

    else:
        pipe_down_pos_x -= 4
        pipe_up_pos_x -= 4

    if going_up:
        bird_pos_y -= 10
        going_up_count += 1
        pygame.transform.rotate(image, 25)
        if going_up_count == 7:
            going_up_count = 0
            going_up = False
    elif not going_up:
        bird_pos_y += 10

    screen.fill((255, 255, 255))
    screen.blit(image_bg, (0, 0))
    screen.blit(image_pipe, (pipe_down_pos_x, pipe_down_pos_y))
    screen.blit(pygame.transform.rotate(image_pipe, 180) , (pipe_up_pos_x, pipe_up_pos_y))

    
    if going_up:
        screen.blit(pygame.transform.rotate(image, 25) , (bird_pos_x, bird_pos_y))

    else:
        screen.fill((255, 255, 255))
        screen.blit(image_bg, (0, 0))
        screen.blit(image_pipe, (pipe_down_pos_x, pipe_down_pos_y))
        screen.blit(pygame.transform.rotate(image_pipe, 180) , (pipe_up_pos_x, pipe_up_pos_y))
        screen.blit(pygame.transform.rotate(image, -25), (bird_pos_x, bird_pos_y))

    if bird_pos_y >= 512 or bird_pos_y < 0:
        game_over = True
      
    # check colision down pipe
    elif bird_pos_y >= pipe_down_pos_y:
        if(pipe_down_pos_x <= bird_pos_x and pipe_down_pos_x > 38):
            game_over = True
        if(pipe_down_pos_x <= bird_pos_x + 30 and pipe_down_pos_x > 38):
            game_over = True
                
    elif bird_pos_y <= pipe_up_pos_y + 320:
        if(pipe_up_pos_x <= bird_pos_x + 30 and pipe_up_pos_x > 38):
            game_over = True
            pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
           going_up = True

    pygame.time.delay(30)
    pygame.display.flip()