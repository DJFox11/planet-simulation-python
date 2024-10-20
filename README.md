# Planet Simulation Project

## Overview
This project is a Python-based simulation of planetary orbits using the `pygame` library. The simulation demonstrates gravitational interactions between celestial bodies, allowing users to visualize the motion of planets around the sun. Newton's law of universal gravitation governs each planet's movement, resulting in a realistic portrayal of planetary motion.

## Features
- Simulates the gravitational forces between planets and the sun.
- Displays the orbital paths of planets as they move over time.
- Provides a visual representation of the solar system with adjustable scaling.
- Dynamically updates each planet's position and velocity based on gravitational forces.

## Requirements
- Python 3.x
- `pygame` library

To install `pygame`, run the following command:
```sh
pip install pygame
```

## How to Run
1. Clone this repository to your local machine.
2. Make sure you have Python and `pygame` installed.
3. Run the `planet_simulation.py` script.

The simulation window will open, showing the sun and various planets orbiting it in real-time.

## Code Structure
### Main Components
- **Planet Class**: The `Planet` class represents a planet with properties such as position, velocity, mass, colour, and radius. It also contains methods to update its position and draw itself on the screen.
- **Gravitational Calculations**: The `attraction` method calculates the gravitational force exerted by other planets using Newton's law of universal gravitation.
- **Simulation Loop**: The `main()` function handles the `pygame` event loop, updating and drawing the planets on each frame.

### Key Variables and Constants
- **Astronomical Unit (AU)**: Used to represent distances in space (in meters).
- **Gravitational Constant (G)**: The gravitational constant used for calculating the force between two bodies.
- **Scale**: The `SCALE` variable adjusts astronomical distances to fit within the window dimensions.
- **Time Step (TIMESTEP)**: Defines the time increment for each frame, which helps control the speed of the simulation.

## Example Planets
The simulation includes several celestial bodies:
- **Sun**: Fixed at the centre of the window, serves as the gravitational source for the other planets.
- **Earth, Mars, Mercury, Venus**: These planets have distinct initial positions, velocities, and masses that define their orbits.

## How It Works
The simulation calculates the gravitational force between the sun and each planet, as well as the forces between the planets themselves. Each planet's velocity and position are updated in every iteration of the simulation loop based on these forces. The planets follow elliptical orbits, similar to real celestial bodies in our solar system.

## Customisation
- You can add more planets or modify the existing ones by altering the `main()` function.
- The initial position, velocity, and mass of each planet can be adjusted to observe different types of orbits.
- Change the `TIMESTEP` value to speed up or slow down the simulation.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
If you have questions, suggestions, or issues, please feel free to open an issue on the repository or reach out to me.
