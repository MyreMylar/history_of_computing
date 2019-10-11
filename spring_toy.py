from math import pi
import pygame
import src.py_particles

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = src.py_particles.Environment((width, height))
universe.colour = (255, 255, 255)
universe.add_functions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.01)
universe.mass_of_air = 0.02

# Add particles here
for p in range(3):
    universe.add_particles(mass=100, size=16, speed=2, elasticity=1, colour=(60, 60, 200))

for p in range(2):
    universe.add_particles(mass=50, size=8, speed=2, elasticity=1, colour=(200, 90, 200))

for p in range(2):
    universe.add_particles(mass=100, size=24, speed=2, elasticity=1, colour=(40, 200, 200))

# join the particles with springs here
universe.add_spring(0, 1, length=100, strength=0.5)
universe.add_spring(1, 2, length=100, strength=0.1)
universe.add_spring(2, 0, length=80, strength=0.05)

universe.add_spring(3, 4, length=150, strength=0.7)

selected_particle = None
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = universe.find_particle(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouse_move(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (0, 0, 0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()

pygame.quit()
