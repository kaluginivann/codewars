# TASK
# Your job is to verify whether a space mission would be successful or not!

# Given a list containing the entire solar system, the destination planet and the megalitres of fuel in the tank, you have to return a boolean that says whether the mission would be successful or not.

# Note that you always launch the spaceship from "Earth".

# The only items that will be in the list are:

# Planets. Any of ["Earth", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]. There will never be more than one of each. There will always be an "Earth" in the list and there will also always be one destination planet in the list. So the list will never be empty and will always have one "Earth" and one other planet at a minimum.
# Asteroids. Zero or more number of asteroids can be present in the Solar System list, though they will never be the destination. Asteroids will also be title cased, like "Asteroid".
# The spaceship would go around all the other objects in the solar system towards the destination_planet. A dictionary is given preloaded under the name fuel_map that has the fuel required in megalitres to go around each planet. It looks like this.

# {
#   "Asteroid": 1,
#   "Mercury": 2,
#   "Venus": 4,
#   "Mars": 3,
#   "Jupiter": 12,
#   "Saturn": 11,
#   "Uranus": 8,
#   "Neptune": 7
# }
# Note: there is no "Earth" in this map as the spaceship should never have to go around "Earth", as it starts from there and there is always only one "Earth"

# Finally, to land, the spaceship needs twice as much fuel required to go around the specific planet, so a spaceship would require 2 * 12, (12 being the amount of fuel required to around "Jupiter"), which is 24 megalitres of fuel to land on "Jupiter".

# Given the megalitres of fuel the spaceship has in it as an integer, you have to return True if the spaceship travels from "Earth" to the destination_planet and lands on it without running out of fuel. If it doesn't, you return False.

# EXAMPLE
# Given the solar system = ["Mercury", "Asteroid", "Earth", "Asteroid", "Saturn", "Venus", "Neptune", "Asteroid"], destination_planet = "Neptune" and fuel = 33, this is what the spaceship would do:

# The spaceship launches from "Earth" towards the right, where "Neptune" is. First the spaceship crosses a "Asteroid", which has a fuel use of 1 to go around in the preloaded fuel_map. So the amount of fuel becomes 32.

# Fuel left: 32

# Then it crosses "Saturn", losing 11 megalitres of fuel.

# Fuel left: 21

# Next it crosses "Venus", losing another 4 megalitres of fuel.

# Fuel left: 17

# Finally it has reached its destination planet, "Neptune", but still needs to land. So it uses 2 * 7 megalitres, which is 14.

# Fuel left: 3

# Done! The spaceship landed on the destination_planet without running out of fuel and you just have to return True. Likewise, if the spaceship had only 20 megalitres it would not be able to make it and you would have to return False in that case.

# In this case the destination_planet, "Neptune", was on the right side of Earth in the list. If the destination planet is on the left side, the space ship simply moves in that direction. So, if the destination_planet for the exact same solar_system as above is "Mercury", the spaceship would launch from "Earth", cross the one "Asteroid" on "Earth"'s left, and then land on "Mercury".

# NOTES
# The fuel integer passed will never be negetive, but it could be 0, in which case any mission is doomed to fail.
# If the spaceship lands on the destination planet with exactly 0 megalitres of fuel left, it is still successful and you should return True.
# The fuel_map is given preloaded. You can use it directly in your code.
# There will always be an "Earth" and the given destination_planet in the Solar System list, so it will never be empty or have only one planet.
# There will always be zero or one of each planet. So there will never be two "Earth"s or two "Jupiter"s. There can be multiple "Asteroid"s though.
# The solar_system input list should not be mutated.
# All planet names and asteroids in the solar_system list or as the destination_planet will always be title-cased.
# There will not be a Pluto in the Solar System.
# Good luck! Hope you, (and most of the missions), are successful!

from preloaded import fuel_map

def successful_mission(solar_system, destination_planet, fuel):
    earth_idx = solar_system.index("Earth")
    dest_idx = solar_system.index(destination_planet)
    
    if dest_idx > earth_idx:
        path = solar_system[earth_idx + 1:dest_idx]
    else:
        path = solar_system[dest_idx + 1:earth_idx]
    
    fuel_needed = sum(fuel_map[obj] for obj in path)
    
    fuel_needed += 2 * fuel_map[destination_planet]
    
    return fuel >= fuel_needed