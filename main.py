import pygame
import sys
import numpy as np

class Particle:
    def __init__(self, x, y, mass):
        self.position = np.array([x, y], dtype=float)
        self.x = x
        self.y = y
        self.velocity = np.array([0.0, 0.0], dtype=float)
        self.force = np.array([0.0, 0.0], dtype=float)
        self.mass = mass

class Spring:
    def __init__(self, particle1, particle2, rest_length, stiffness):
        self.particle1 = particle1
        self.particle2 = particle2
        self.rest_length = rest_length
        self.stiffness = stiffness

def generate_particles(number=5,radius=50,mass=1):
    # Position of particles starting at (rad,0)
    dtheta = 2 * np.pi / number
    particle_list = []
    for theta in np.arange(0,2*np.pi,dtheta):
        x, y = radius * np.cos(theta), radius * np.sin(theta)
        particle = Particle(x,y,mass);
        particle_list.append(particle);
    return particle_list

def generate_springs(particle_list=[],stiffness=1):
    a = list(range(0,len(particle_list)))
    b = a[1:] + a[:1]
    spring_list = []
    for (i,j) in zip(a,b):
        p1 = particle_list[i]
        p2 = particle_list[j]
        dist = np.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
        sp = Spring(p1,p2,dist,stiffness)
        spring_list.append(sp)
    return spring_list

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Circle Simulation")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    # Update the physics simulation here
    particles = generate_particles(10,150)
    springs = generate_springs(particles,1)

    # Clear the screen
    SCREEN.fill(BACKGROUND_COLOR)

    # Render particles and springs here
    for spring in springs:
        p1 = spring.particle1
        p2 = spring.particle2
        # Convert particle positions to integers for drawing
        p1_pos = (int(p1.position[0]) + (WIDTH // 2), int(p1.position[1]) + (HEIGHT // 2))
        p2_pos = (int(p2.position[0]) + (WIDTH // 2), int(p2.position[1]) + (HEIGHT // 2))
        # print(p1_pos,p2_pos)
        # Draw a line to represent the spring
        pygame.draw.line(SCREEN, (0, 0, 0), p1_pos, p2_pos, 2)
        # (0, 0, 0) is the color, and 2 is the line width

    # Your code to render particles as circles goes here
    for particle in particles:
        offset_x = int(particle.x) + (WIDTH // 2)
        offset_y = int(particle.y) + (HEIGHT // 2)
        pygame.draw.circle(SCREEN, (255, 0, 0), (offset_x, offset_y), 5)
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
