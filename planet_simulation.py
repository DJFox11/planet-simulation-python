import pygame
import math
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Define colors for the planets
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

# Font for displaying text on the screen
FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    # Constants used in the simulation
    AU = 149.6e6 * 1000  # Astronomical Unit in meters
    G = 6.67428e-11  # Gravitational constant
    SCALE = 250 / AU  # Scale for rendering distance on the screen
    TIMESTEP = 3600 * 24  # One day in seconds

    def __init__(self, x, y, radius, color, mass):
        # Initialize the planet's attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []  # List to store the orbit points for drawing
        self.sun = False  # Flag to determine if the planet is the sun
        self.distance_to_sun = 0  # Distance to the sun (used for display)

        self.x_vel = 0  # Initial x velocity
        self.y_vel = 0  # Initial y velocity

    def draw(self, win):
        # Calculate position on the screen based on scaling
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # Draw the orbit path if it has more than two points
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)  # Draw the orbit path

        # Draw the planet
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # Display distance to the sun if the planet is not the sun
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        # Calculate the gravitational attraction force exerted by another planet
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)  # Distance between the two planets

        # If the other planet is the sun, update the distance to the sun
        if other.sun:
            self.distance_to_sun = distance

        # Calculate the gravitational force
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)  # Angle between the planets
        force_x = math.cos(theta) * force  # x component of the force
        force_y = math.sin(theta) * force  # y component of the force
        return force_x, force_y
    
    def update_position(self, planets):
        # Update the position of the planet based on gravitational forces from other planets
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue  # Skip itself

            # Calculate the force exerted by the other planet
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # Update velocities based on the net force and timestep
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # Update positions based on velocity and timestep
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))  # Add current position to the orbit list

def main():
    # Main function to run the simulation
    run = True
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    # Create instances of planets
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True  # Mark this planet as the sun

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000  # Set initial velocity for Earth's orbit

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000  # Set initial velocity for Mars' orbit

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000  # Set initial velocity for Mercury's orbit

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000  # Set initial velocity for Venus' orbit

    planets = [sun, earth, mars, mercury, venus]  # List of all planets in the simulation

    while run:
        clock.tick(60)  # Limit the frame rate to 60 frames per second
        WIN.fill((0, 0, 0))  # Fill the screen with black color to clear previous frame

        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the loop if the user closes the window

        # Update positions and draw all planets
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()  # Update the display with the new frame

    pygame.quit()  # Quit pygame when the loop ends

main()
