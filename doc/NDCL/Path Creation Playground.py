#Path Creation Playground
import numpy as np
import matplotlib.pyplot as plt

step_number = 50

theta = np.linspace(-np.pi/2,np.pi/2,step_number)[:, np.newaxis]
x = np.cos(theta)
y = np.sin(theta)

phi = np.linspace(0,2*np.pi,step_number)[:, np.newaxis]
z = np.sin(phi)

x_offset = 0.145
y_offset = 0
z_offset = 0.09 + 0.2

x_bar = x * 0.2 + x_offset
y_bar = y * 0.2 + y_offset
z_bar = z * 0.15 + z_offset

pose_data = np.hstack((x_bar, y_bar, z_bar))

plt.subplot(1,2,1)
plt.plot(pose_data[:,0], pose_data[:,1])

plt.subplot(1,2,2)
plt.plot(range(len(pose_data[:,2])),pose_data[:,2])
plt.show()

ax = plt.figure().add_subplot(projection='3d')

ax.plot(pose_data[:,0], pose_data[:,1], pose_data[:,2])  # Plot contour curves

plt.show()

import numpy as np

returning = np.array(((0,0,0.3),(0.2,0,0),(-0.1,0.15,0),(-0.1,0.15,0),(0,0.15,0),(0,-0.15,0),(0.1,-0.15,0),(0.1,-0.15,0),(-0.2,0,0),(0,0,-0.3)))

waypoints = np.array(((0,0,0.3),(0.2,0,0),(-0.1,0.15,0),(-0.1,0.15,0),(0,0.15,0)))

mirrored_waypoints = flipud(-waypoints)

waypoints = np.vstack((waypoints, mirrored_waypoints))

zero = returning - waypoints