import pygame
import numpy as np

pygame.init()
WIDTH = 800
HEIGHT = 800
window  = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_CENTER = np.array([WIDTH/2, HEIGHT/2], dtype=np.float64)
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = np.array([WIDTH/2, HEIGHT/2 -120], dtype=np.float64)
running = True
GRAVITY = 0.2
ball_vel = np.array([0,0], dtype=np.float64)  
#ball velocity

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        ball_vel[1] += GRAVITY # Apply gravity to the ball's vertocal velocity
        #ball_vel[1] = ball_vel [1] + GRAVITY
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        # Update the ball's position based on its velocity
        dist = np.linalg.norm(ball_pos - CIRCLE_CENTER)
        # Check if the ball is outside the circle
        if dist + BALL_RADIUS > CIRCLE_RADIUS:
            d = ball_pos - CIRCLE_CENTER
            t = np.array([-d[1],d[0]], dtype=np.float64)
            proj_v_t = (np.dot(ball_vel, t)/np.dot(t, t)) * t 
            # Calculate the projection of the ball's velocity onto the tangent vector
            ball_vel = 2 * proj_v_t - ball_vel
        window.fill(BLACK)
        pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
        # Draw the circle at the center
        pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)
        #draw the red ball 
        pygame.display.flip()
        clock.tick(60)

pygame.quit()