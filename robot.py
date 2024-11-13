import pygame
import sys

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Challenging Maze Robot Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

robot_size = 20
robot_x, robot_y = 60, 60  
robot_speed = 5

wall_thickness = WIDTH * 0.015 


walls = [

    pygame.Rect(0, 0, WIDTH, wall_thickness),              
    pygame.Rect(0, 0, wall_thickness, HEIGHT),             
    pygame.Rect(WIDTH - wall_thickness, 0, wall_thickness, HEIGHT),  
    pygame.Rect(0, HEIGHT - wall_thickness, WIDTH, wall_thickness),  

    pygame.Rect(WIDTH * 0.05, HEIGHT * 0.1, wall_thickness, HEIGHT * 0.8),
    pygame.Rect(WIDTH * 0.2, HEIGHT * 0.05, wall_thickness, HEIGHT * 0.7),
    pygame.Rect(WIDTH * 0.25, HEIGHT * 0.2, wall_thickness, HEIGHT * 0.6),
    pygame.Rect(WIDTH * 0.3, HEIGHT * 0.3, wall_thickness, HEIGHT * 0.5),
    pygame.Rect(WIDTH * 0.4, HEIGHT * 0.15, wall_thickness, HEIGHT * 0.75),
    pygame.Rect(WIDTH * 0.45, HEIGHT * 0.2, wall_thickness, HEIGHT * 0.5),
    pygame.Rect(WIDTH * 0.5, HEIGHT * 0.05, wall_thickness, HEIGHT * 0.7),
    pygame.Rect(WIDTH * 0.6, HEIGHT * 0.25, wall_thickness, HEIGHT * 0.6),
    pygame.Rect(WIDTH * 0.65, HEIGHT * 0.35, wall_thickness, HEIGHT * 0.6),
    pygame.Rect(WIDTH * 0.75, HEIGHT * 0.1, wall_thickness, HEIGHT * 0.8),
    pygame.Rect(WIDTH * 0.8, HEIGHT * 0.25, wall_thickness, HEIGHT * 0.7),
    pygame.Rect(WIDTH * 0.85, HEIGHT * 0.5, wall_thickness, HEIGHT * 0.4),
    pygame.Rect(WIDTH * 0.9, HEIGHT * 0.2, wall_thickness, HEIGHT * 0.6),
    pygame.Rect(WIDTH * 0.9, HEIGHT * 0.75, wall_thickness, HEIGHT * 0.25),
]

finish_line = pygame.Rect(WIDTH - 80, HEIGHT - 80, 40, 40)

won = False  
game_over = False  

def reset_game():
    global robot_x, robot_y, won, game_over
    robot_x, robot_y = 60, 60  
    won = False
    game_over = False

while True:
    screen.fill(WHITE)  
    pygame.time.delay(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= robot_speed
    if keys[pygame.K_RIGHT]:
        robot_x += robot_speed
    if keys[pygame.K_UP]:
        robot_y -= robot_speed
    if keys[pygame.K_DOWN]:
        robot_y += robot_speed

    robot = pygame.Rect(robot_x, robot_y, robot_size, robot_size)

    for wall in walls:
        if robot.colliderect(wall):
            game_over = True  
            reset_game()  
            break 

    if robot.colliderect(finish_line):
        won = True
        break  

    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    pygame.draw.rect(screen, GREEN, finish_line)
    pygame.draw.rect(screen, BLUE, robot)

    if won:
        font = pygame.font.Font(None, 50)
        text = font.render("Congratulations! You've finished the maze!", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  
        screen.blit(text, text_rect)
    elif game_over:
        font = pygame.font.Font(None, 50)
        text = font.render("You hit a wall! Restarting...", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

    if won or game_over:
        pygame.time.delay(2000)

pygame.quit()
