import numpy as np
import matplotlib.pyplot as plt
# Read the image
m = plt.imread("/home/rguktrkvalley/Pictures/recent_addiction.jpg")

# Split channels
red = m[:, :, 0]
green = m[:, :, 1]
blue = m[:, :, 2]

# Save each channel to a CSV file
np.savetxt("red.csv", red.flatten(), delimiter=",")
np.savetxt("green.csv", green.flatten(), delimiter=",")
np.savetxt("blue.csv", blue.flatten(), delimiter=",")
