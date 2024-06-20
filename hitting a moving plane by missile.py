import matplotlib.pyplot as plt
from numpy import cos, sin, radians, linspace
from scipy.optimize import fsolve

# Given parameters
u = 15  # Initial speed of the projectile (m/s)
a, b = 10, 8  # Initial position of the target
vx_target = 8  # Velocity of the target in the x-direction (m/s)
vy_target = -5  # Velocity of the target in the y-direction (m/s)
g = 9.81  # Acceleration due to gravity (m/s^2)

# Define the system of equations
def equations(vars):
    theta, t = vars
    eq1 = u * cos(radians(theta)) * t - (a + vx_target * t)
    eq2 = u * sin(radians(theta)) * t - 0.5 * g * t**2 - (b + vy_target * t)
    return [eq1, eq2]

# Initial guess for the variables
initial_guess = [85, 1]  # theta in degrees, t in seconds

# Solve the system of equations
solution = fsolve(equations, initial_guess)
theta, t = solution

# Verify the solution
x_missile_hit = u * cos(radians(theta)) * t
y_missile_hit = u * sin(radians(theta)) * t - 0.5 * g * t**2
x_target_hit = a + vx_target * t
y_target_hit = b + vy_target * t

hit_tolerance = 1e-6  # Tolerance for considering the hit valid

if abs(x_missile_hit - x_target_hit) < hit_tolerance and abs(y_missile_hit - y_target_hit) < hit_tolerance and t > 0:
    print(f'Solution is valid: theta = {theta} degrees, t = {t} seconds')
    hit_valid = True
else:
    print(f'Solution is not valid: theta = {theta} degrees, t = {t} seconds')
    hit_valid = False
    print("The missile does not hit the target.")

# Plotting the trajectory
t_values = linspace(0, t, 100)
x_missile = u * cos(radians(theta)) * t_values
y_missile = u * sin(radians(theta)) * t_values - 0.5 * g * t_values**2

# If missile misses the target, plot until it falls to the ground
if not hit_valid:
    max_time = 2 * u * sin(radians(theta)) / g  # Time to fall to ground after peak
    t_values = linspace(0, max_time, 100)
    x_missile= u * cos(radians(theta)) * t_values
    y_missile = u * sin(radians(theta)) * t_values - 0.5 * g * t_values**2
    
# Plot target and initial position
plt.scatter([10], [8], color='red', label='Target start (a=10, b=8)')
plt.plot([a, a + vx_target * t_values.max()], [b, b + vy_target * t_values.max()], linestyle='--', color='orange', label='Target path')

# Plot the missile trajectory
plt.plot(x_missile, y_missile, label='Missile')

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Projectile and Target Trajectory with u={u}')
plt.legend()
plt.grid(True)
plt.show()
