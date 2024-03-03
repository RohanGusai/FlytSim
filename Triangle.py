#!/usr/bin/env python
import time
from flyt_python import api

# Instance of the Flyt droneigation class
drone = api.navigation(timeout=120000)

# At least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

# Take off
print('Taking off')
drone.take_off(5.0)

# Define the vertices of the triangle
vertices = [(5, 0, 0), (-2.5, 8.66, 0), (-2.5, -8.66, 0)]

# Move to each vertex
print('Moving along the setpoints to form a triangle')
for vertex in vertices:
    drone.position_set(*vertex, relative=True)

# Land
print('Landing')
drone.land(async=False)

# Shutdown the instance
drone.disconnect()

~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                   
